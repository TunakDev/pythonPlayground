import pypandoc

# first time running needs the pandoc program to be installed
# from pypandoc.pandoc_download import download_pandoc
# see the documentation how to customize the installation path
# but be aware that you then need to include it in the `PATH`
# download_pandoc()

output = pypandoc.convert_file('../../openwebui/data/<anonFile>', 'plain', outputfile="data/data.txt")
assert output == ""