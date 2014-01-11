# /usr/bin/env python2

from gimpfu import *

def pythonfu_triangsaic(img, layer, blockSize, multiple, mergeFlag):
    # Initializes the main parameters
    height = pdb.gimp_image_height(img)

    # First rotation
    layerOne = pdb.gimp_layer_copy(layer, pdb.gimp_drawable_has_alpha(layer))
    pdb.gimp_item_set_name(layerOne,"Pixelation one")
    pdb.gimp_image_insert_layer(img,layerOne, None, -1)
    pdb.gimp_item_transform_shear(layerOne,0,height*multiple)
    pdb.plug_in_pixelize2(img,layerOne, blockSize, blockSize)
    pdb.gimp_item_transform_shear(layerOne,0,-height*multiple)

    # Second rotation
    layerTwo = pdb.gimp_layer_copy(layer, pdb.gimp_drawable_has_alpha(layer))
    pdb.gimp_item_set_name(layerTwo,"Pixelation two")
    pdb.gimp_image_insert_layer(img,layerTwo, None, -1)
    pdb.gimp_item_transform_shear(layerTwo,0,-height*multiple)
    pdb.plug_in_pixelize2(img,layerTwo, blockSize, blockSize)
    pdb.gimp_item_transform_shear(layerTwo,0,height*multiple)
    pdb.gimp_layer_set_opacity(layerTwo, 50)

    # Merge the layers
    if mergeFlag:
        mergedLayer = pdb.gimp_image_merge_down(img,layerTwo,0)
        mergedLayer = pdb.gimp_image_merge_down(img,mergedLayer,0)
    return

register(
        "pythonfu_triangsaic",
        "Creates a triangle pixelation effect",
        "Creates a triangle pixelation effect",
        "Alex Sanchez (Kniren)",
        "Alex Sanchez (Kniren)",
        "2014",
        "<Image>/Filters/Blur/Triangle Pixelation...",
        "*",
        [
            (PF_INT, "blockSize", "Pixelation size", 40),
            (PF_INT, "multiple", "Multiple of the triangle", 1),
            (PF_TOGGLE, "mergeFlag", "Do you want to merge the layers?", 1)
        ],
        [],
        pythonfu_triangsaic
        )

main()
