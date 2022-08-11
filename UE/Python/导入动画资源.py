import  unreal

def buildImportTask(filename, destination_path, options=None):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    task.set_editor_property('options', options)
    return task

def executeImportTasks(tasks : unreal.AssetImportTask):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            print('Imported: %s ' % path)

def importMyAssets():
    importAnimationAssets()

def importSimpleAssets():
    texture_tga = 'C:/Users/gaolei08/Pictures/aa.tga'
    sound_wav = 'C:/Users/gaolei08/Pictures/bb.wav'

    textture_task = buildImportTask(texture_tga, '/Game/Textures')
    sound_task = buildImportTask(sound_wav, '/Game/Sounds')
    executeImportTasks([textture_task, sound_task])

def importAnimationAssets():
    animation_fbx = 'C:/Users/gaolei08/Pictures/animation.fbx'
    animation_fbx_task = buildImportTask(animation_fbx, '/Game/Animations',
        buildAnimationImportOptions('/Game/SkeletalMeshs/SK_SkeletalMesh_Skeleton'))#需要指定导入的动画骨架
    executeImportTasks([animation_fbx_task])

def buildAnimationImportOptions(skeleton_path):
    options = unreal.FbxImportUI()

    options.set_editor_property('import_animations', True)
    options.skeleton = unreal.load_asset(skeleton_path)

    options.anim_sequence_import_data.set_editor_property('import_translation', unreal.Vector(0.0, 0.0, 0.0))
    options.anim_sequence_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 0.0, 0.0))
    options.anim_sequence_import_data.set_editor_property('import_uniform_scale', 1.0)

    options.anim_sequence_import_data.set_editor_property('animation_length', unreal.FBXAnimationLengthImportType.FBXALIT_EXPORTED_TIME)
    options.anim_sequence_import_data.set_editor_property('remove_redundant_keys', False)
    return options
