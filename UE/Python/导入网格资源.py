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
    importMeshAssets()

def importMeshAssets():
    static_mesh_fbx = 'D:/YY55/MaterSour/sm_pine_02.FBX'
    skeletal_mesh_fbx = 'D:/YY55/MaterSour/sm_skeletal_02.FBX'
    static_mesh_task = buildImportTask(static_mesh_fbx, '/Game/StaticMeshs', buildStaticMeshImportOptions())
    skeletal_mesh_task = buildImportTask(skeletal_mesh_fbx, '/Game/SkeletalMeshs', buildSkeletalMeshImportOptions())
    executeImportTasks([static_mesh_task, skeletal_mesh_task])


def importSimpleAssets():
    texture_tga = 'C:/Users/gaolei08/Pictures/aa.tga'
    sound_wav = 'C:/Users/gaolei08/Pictures/bb.wav'

    textture_task = buildImportTask(texture_tga, '/Game/Textures')
    sound_task = buildImportTask(sound_wav, '/Game/Sounds')
    executeImportTasks([textture_task, sound_task])


def buildStaticMeshImportOptions():
    options = unreal.FbxImportUI()

    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_textures', False)
    options.set_editor_property('import_materials', True)
    options.set_editor_property('import_as_skeletal', False)

    options.static_mesh_import_data.set_editor_property('import_translation', unreal.Vector(50.0, 0.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 10.0, 0.0))
    options.static_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)

    options.static_mesh_import_data.set_editor_property('combine_meshes', True)
    options.static_mesh_import_data.set_editor_property('generate_lightmap_u_vs', True)
    options.static_mesh_import_data.set_editor_property('auto_generate_collision', True)
    return options

def buildSkeletalMeshImportOptions():
    options = unreal.FbxImportUI()

    options.set_editor_property('import_mesh', True)
    options.set_editor_property('import_texture', False)
    options.set_editor_property('import_materials', True)
    options.set_editor_property('import_as_skeletal', True)

    options.skeletal_mesh_import_data.set_editor_property('import_translation', unreal.Vector(50.0, 0.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property('import_rotation', unreal.Rotator(0.0, 10.0, 0.0))
    options.skeletal_mesh_import_data.set_editor_property('import_uniform_scale', 1.0)

    options.skeletal_mesh_import_data.set_editor_property('import_morph_targets', True)
    options.skeletal_mesh_import_data.set_editor_property('undate_skeleton_reference_pose', False)
    return options