import  unreal

texture_tga = 'C:/Users/gaolei08/Pictures/aa.tga'
sound_wav = 'C:/Users/gaolei08/Pictures/bb.wav'

def buildImportTask(filename, destination_path):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', '')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', True)
    task.set_editor_property('save', True)
    return task

def executeImportTasks(tasks : unreal.AssetImportTask):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    for task in tasks:
        for path in task.get_editor_property('imported_object_paths'):
            print('Imported: %s ' % path)

def importMyAssets():
    texture_task = buildImportTask(texture_tga, '/Game/Textures')
    sound_task = buildImportTask(sound_wav, '/Game/Sounds')
    executeImportTasks([texture_task, sound_task])
