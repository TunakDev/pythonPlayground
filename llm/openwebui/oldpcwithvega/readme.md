# To run Ollama on an old gaming PC and use the network to prompt this model using Open WebUI

In the following article I'll explain how to run a model on an old PC with an AMD Vega 56 (gfx900:xnack-).

Let the old gaming PC be named "MODEL_RUNNER" and the PC running Open WebUI "UI_RUNNER".

## First for the not so easy, easy part:

For first time:
-- Install AMD Driver 22.7.1 (AMD Software Adrenalin Edition)
-- Install ROCm 5.7 from official website
-- Install https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170 (this fixes error 0xc000005 as stated in the guide)
-- ADD THE FUCKING ROCM PATH (C:/Programs/AMD/ROCm/5.7/bin) to the system variable PATH (this fixes error 0xc000005 as stated in the guide)

ollama prerequisites
-- download ollama for amd
-- close ollama service (tray in windows bottom right on desktop)
-- replace lib and ollama.exe with the ones for amd-rocm5.7z
-- replace rocblas.dll in /Ollama/lib/ollama/rocm with file from rocm-gfx900-xnack--HIP.SDK.5.7.7z
-- delete (!) library in /Ollama/lib/ollama/rocm/rocblas
-- replace add the folder library from rocm-gfx900-xnack--HIP.SDK.5.7.7z to where the deleted one was

start ollama
-- cmd "ollama serve"
-- another (!) cmd "ollama run llama3.2"



At first (because I already stumbled there) you have to install graphics drivers. For me and my GPU this was the
AMD Software Adrenalin Edition in Version 22.7.1

And I do not know why since the guide tells us not to do it but I had to install the official ROCm version from the AMD homepage in Version 5.7.1.
Afterwards I switched the files like told below and in the guide in the ollama, ollama/rocm and ollama/rocblas directories. Just all of them...
Somehow it magically worked afterwards

??????????

Download newest version of ollama first and swap files afterwards 


??????????

On the MODEL_RUNNER you need to install Ollama-for-amd: https://github.com/likelovewant/ollama-for-amd/releases
and follow the instructions there. I used this video as help: https://www.youtube.com/watch?v=G-kpvlvKM1g
Hint: For my Vega 56 I used the 'ollama-windows-amd64-rocm5.7z', extracted it to the standard installation location of ollama (%localappdata%/programs/Ollama) and then downloaded the ROCm-Libs (rocm-gfx900-xnack--HIP.SDK.5.7.7z) from https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU/releases/tag/v0.5.7 
Afterwards you just switch the files as described (rocblas.dll and library).

SOMETIMES - NOT ALL THE TIME - THIS CAN CAUSE AN ERROR You then have to set the environment variable "HSA_OVERRIDE_GFX_VERSION=9.0.0" for the Vega 56.

Important: After you installed it and switched the rocblas-files you need to restart the service (or just your system)
then bind the host-adress of ollama to 0.0.0.0 using 'set OLLAMA_HOST=0.0.0.0:11434' and then use 'ollama serve' to run ollama.

Sidenote: If you don't use ollama for a while using 'serve' it needs a bit to reload the model when prompted. I'm sure you can avoid this using settings somehow...

When you've done this you can download a model and run it in another cmd-window using e.g. 'ollama run llama3.1 --verbose'
and enjoy the way higher tokens/s than using the CPU.
You can also check whether the model is running on the CPU or the GPU using 'ollama ps' or other ways described in this video: https://www.youtube.com/watch?v=on3rtyPWSgA

After ollama and the model are up and running you can check the connection to the MODEL_RUNNER using 
'curl http://{ip-adress-of-model-runner}:11434/api/tags'.
This should give you a JSON-list of all available models of ollama

You can find the IP using e.g. netstat in a cmd window on the MODEL_RUNNER. It should be something about '192.168.X.X'

## Now the easy part

On the UI_RUNNER you just have to install Docker and run docker-compose with the linked docker-compose.yaml

I've made some important changes to the file:
- environment: "OLLAMA_BASE_URL" -> This is the URL under which Ollama on the MODEL_RUNNER-Server can be found.
- environment: "WEBUI_AUTH=FALSE" -> This helps the development since no account is needed. This is a security issue once this is deployed on an accessible Server!
- "privileged:true" -> this was needed since open-webui was not allowed to start multiple processes. I think you can counter this with settings in Docker itself but this was the faster way to get a PoC running.

If the container is up and running just go to 'localhost:3000' and you should be able to access the UI of Open WebUI.

Here you can just prompt the model or build some fancy RAG (Retrieval Augmented Generation)

To use RAG you can now create a "Knowledge" using "Workspace" in the left sidebar, then use the tab "Knowledge" on top. 
Here you can create a Knowledge and after creation add files to it (preferably in markdown - .md - format).
After creating the Knowledge go back to the tab "Models" and create a new model, give it a simple system prompt and add the Knowledge further down in the configuration.
Then click "save & create" and you can use it using "New Chat" in the upper left corner. Choose the new model and get going!
The fancy part is that it shows you the referred files just below the answer. Great feature!