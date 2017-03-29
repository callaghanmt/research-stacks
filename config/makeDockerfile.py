mylist = ["00_os_ubuntu_latest", "34_app_emacs", "18_lib_vtk"]

def create_Dockerfile(fragmentList):
    fragmentList.sort()

    Dockerfile = ""
    for fragment in fragmentList:
        fragmentfile = open(fragment, "r")
        Dockerfile = Dockerfile + fragmentfile.read()
        fragmentfile.close()

    return Dockerfile

