import argostranslate.package
import argostranslate.translate
import enchant


def translateEnToRu(string):
    d = enchant.Dict("en_US")

    from_code = "en"
    to_code = "ru"

    # Download and install Argos Translate package
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    package_to_install = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code, available_packages
        )
    )
    if package_to_install not in argostranslate.package.get_installed_packages():
        argostranslate.package.install_from_path(package_to_install.download())

    return argostranslate.translate.translate(
        string, from_code, to_code
    )


if __name__ == "__main__":
    print(translateEnToRu("I ran, fuck, and I fell, fuck, and I was shot."))
