from ScriptCollection.GeneralUtilities import Platform
from ScriptCollection.TFCPS.Docker.TFCPS_CodeUnitSpecific_Docker import TFCPS_CodeUnitSpecific_Docker_Functions,TFCPS_CodeUnitSpecific_Docker_CLI

 
def build():
    tf:TFCPS_CodeUnitSpecific_Docker_Functions=TFCPS_CodeUnitSpecific_Docker_CLI.parse(__file__)
    tf.build([
            Platform.Linux_AMD64,
            Platform.Linux_ARM64,
        ],{
            "image_alpine":tf.tfcps_Tools_General.oci_image_manager.get_registry_address_for_image_with_default_tag(tf.get_repository_folder(),"Alpine"),
            "image_go":tf.tfcps_Tools_General.oci_image_manager.get_registry_address_for_image_with_default_tag(tf.get_repository_folder(),"Go"),
        }
    )
    #TODO add sbom from alpine image to sbom of this codeunit

if __name__ == "__main__":
    build()
