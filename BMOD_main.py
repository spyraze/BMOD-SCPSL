# To make this add-on installable, create an extension with it:
# https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html
bl_info = {
        "name":"BAMER - Blender Addon for Map Editor Reborn for SCP:SL",
        "author":"Spyblaze",
        "version":"0.1",
        "blender":(4,3),
        "description":"Converts blender mesh into json filel which can be used to make objects for server easily"
}
number_of_quads=0
import bpy
import bpy
from bpy import context
import bmesh
import pprint
import json
import pathlib
import math
import os
import subprocess
import shutil
from pathlib import Path
import random
from bpy.types import (Panel,Operator) 





class Blend_To_Json_Convertor(bpy.types.Operator):
    """Tooltip"""
    
    #god knows what this does
    bl_idname = "neviem.1"
    bl_label = "neviem2"



    #executes code after pressing Convert Button
    def execute(self, context):
        

        #def start():
            
            #tries to get if object has mesh
            
       #Defines variables for path,save, color, face verts and location of verts
        file_path = Path(bpy.context.scene.my_tool.foo)
        path_to_file = pathlib.Path.home() / bpy.context.scene.my_tool.foo / "mesh.json"
        base_color=[]
        face_verts=[]
        vert_coords = []
        
        #makes vert faces
        
                
        def get_json(rotation, scale, poloha_objekt):
            obj = bpy.context.active_object
            object_name = obj.name
            id=random.randint(0,10000000)
            primitive_type=""
            base_color=[]
            poloha_objekt=[]
            scale=[]
            rotation=[]

            if object_name[:8]=="Cylinder" or object_name[:6]=="Plane" or object_name[:5]=="Cube" or object_name[:7]=="Capsule" or object_name[:7]=="Sphere":
                
                a=0
                
                bpy.ops.object.mode_set(mode="OBJECT")
                bpy.ops.object.mode_set(mode="EDIT")
                obj = bpy.context.edit_object
                me = obj.data
                bm = bmesh.from_edit_mesh(me)
                
                
                if object_name[:5]=="Cube":
                    primitive_type=3
                    bpy.ops.object.mode_set(mode="OBJECT")
                    poloha_objekt.append(list(list(obj.location)))
                    scale.append(list(list(obj.scale)))


                    face_verts.append(1)
                    rot3_axis = list(obj.rotation_euler)
                    aj=[0,0,0]
                    rotation.append(aj)
                    for i in range(3):
                        rotation[0][i]=(rot3_axis[i]*180/3.14)
                        rotation[0][i]=round(rotation[0][i],1)
                        color=list(obj.color)
                        color = '#%02x%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(color[3] * 255))
                        base_color.append(str(color))
                        color=[]
                    rotation[0][0]=rotation[0][0]*(-1)

                if object_name[:6]=="Plane":
                    primitive_type=5
                    bpy.ops.object.mode_set(mode="OBJECT")
                    poloha_objekt.append(list(list(obj.location)))
                    scale.append(list(list(obj.scale)))


                    face_verts.append(1)
                    rot3_axis = list(obj.rotation_euler)
                    aj=[0,0,0]
                    rotation.append(aj)
                    for i in range(3):
                        rotation[0][i]=(rot3_axis[i]*180/3.14)
                        rotation[0][i]=round(rotation[0][i],1)
                        color=list(obj.color)
                        color = '#%02x%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(color[3] * 255))
                        base_color.append(str(color))
                        color=[]
                    rotation[0][0]
                    rotation[0][0]=rotation[0][0]*(-1)
                if object_name[:8]=="Cylinder":
                    primitive_type=2
                    bpy.ops.object.mode_set(mode="OBJECT")
                    poloha_objekt.append(list(list(obj.location)))
                    scale.append(list(list(obj.scale)))


                    face_verts.append(1)
                    rot3_axis = list(obj.rotation_euler)
                    aj=[0,0,0]
                    rotation.append(aj)
                    for i in range(3):
                        rotation[0][i]=(rot3_axis[i]*180/3.14)
                        rotation[0][i]=round(rotation[0][i],1)
                        color=list(obj.color)
                        color = '#%02x%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(color[3] * 255))
                        base_color.append(str(color))
                        color=[]
                    rotation[0][0]
                    rotation[0][0]=rotation[0][0]*(-1)    
                if object_name[:7]=="Capsule":
                    primitive_type=1
                    bpy.ops.object.mode_set(mode="OBJECT")
                    poloha_objekt.append(list(list(obj.location)))
                    scale.append(list(list(obj.scale)))
                    scale[0][1]=scale[0][1]/2

                    face_verts.append(1)
                    rot3_axis = list(obj.rotation_euler)
                    aj=[0,0,0]
                    rotation.append(aj)
                    for i in range(3):
                        rotation[0][i]=(rot3_axis[i]*180/3.14)
                        rotation[0][i]=round(rotation[0][i],1)
                        color=list(obj.color)
                        color = '#%02x%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(color[3] * 255))
                        base_color.append(str(color))
                        color=[]
                    rotation[0][0]=rotation[0][0]*(-1) 
                if object_name[:7]=="Sphere":
                    primitive_type=0
                    bpy.ops.object.mode_set(mode="OBJECT")
                    poloha_objekt.append(list(list(obj.location)))
                    scale.append(list(list(obj.scale)))
                    scale[0][1]=scale[0][1]/2

                    face_verts.append(1)
                    rot3_axis = list(obj.rotation_euler)
                    aj=[0,0,0]
                    rotation.append(aj)
                    for i in range(3):
                        rotation[0][i]=(rot3_axis[i]*180/3.14)
                        rotation[0][i]=round(rotation[0][i],1)
                        color=list(obj.color)
                        color = '#%02x%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(color[3] * 255))
                        base_color.append(str(color))
                        color=[]
                    rotation[0][0]=rotation[0][0]*(-1) 
            else:
                if object_name[:6]=="Point":
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")
                    print("")


                    color=list(obj.data.color)
                    light_color = '#%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
                    print(light_color )
                    base_color.append(str(light_color).upper())


                    bpy.ops.object.mode_set(mode="OBJECT")
                    poloha_objekt.append(list(list(obj.location)))
                    aj=[0,0,0]
                    rotation.append(aj)
                    aj=[0,0,0]
                    scale.append(aj)
            data1={}
            print( poloha_objekt)
            data1={
                    "Name": str(id),
                    "ObjectId": id,
                    "ParentId":  23126,
                    "Position":{
                        "x": poloha_objekt[0][0],
                        "y":poloha_objekt[0][2],
                        "z":poloha_objekt[0][1]
                    },
                    "Rotation":{
                        "x": rotation[0][0],
                        "y": rotation[0][2],
                        "z": rotation[0][1]
                    },
                    "Scale":{
                        "x": scale[0][0],
                        "y": scale[0][2],
                        "z": scale[0][1]
                    },
                    "BlockType": 1,
                }
            if base_color==[]:
                base_color="FFFFFFFF"
            if object_name[:6]=="Point":
                del data1["Rotation"]
                del data1["Scale"]
                data1["BlockType"]=2
                data1["Properties"]={
                "Color": base_color[0].upper(),
                "Intensity": obj.data.energy,
                "Range": obj.data.shadow_soft_size,
                "Shadows": obj.data.use_shadow
                 }
            if primitive_type!="":

                data1["Properties"]={
                "PrimitiveType": primitive_type,
                "Color": base_color[0].upper(),
                "PrimitiveFlags": 3
      
                }
            
            blocks.append(data1)
                
            
            a=0
            
            
            data={
                "RootObjectId":  23126,
                "Blocks": blocks
            
            }
            
            

            with open(path_to_file, "w") as out_file_obj:
                 # convert the dictionary into text
                text = json.dumps(data, indent=4)
                # write the text into the file
                out_file_obj.write(text)
               
        def Main(blocks):
            rotation=[]
            scale=[]
            poloha_objekt=[]
            #start()
          
            
           
            
            get_json(rotation, scale,poloha_objekt)
            
            bpy.ops.object.mode_set(mode="OBJECT")
        
        blocks=[]
        id_objekt=0
        def select_multiple(file_path):
           

            scene = bpy.context.scene

            a=0
           

        # Loop through all objects in the scene
            for obj in range(len(scene.objects)):
            # Deselect all objects
               
                obj_name = scene.objects[a].name
                obj = scene.objects.get(obj_name)
                obj.select_set(True)
            # Select the current object
                bpy.context.view_layer.objects.active = obj
            # Optionally, you can do something with the selected object here
                
                Main(blocks)

                a+=1
                obj.select_set(False)
            
            if (file_path/"mesh").exists():
                
                
                shutil.rmtree(file_path/"mesh")
            
            
            folder_path = file_path.parent
            
            if folder_path != " ":
                os.startfile(folder_path/"Schematics")
             
            

        select_multiple(file_path)

        return {'FINISHED'}

from bpy.props import (StringProperty,
                       PointerProperty,
                       )
                       
from bpy.types import (Panel,
                       PropertyGroup,
                       )
        
class MyProperties(PropertyGroup):

    foo: StringProperty(
        name="Schematics_Path",
        description=":",
        default="",
        maxlen=1024,
        )

    





class OBJECT_PT_CustomPanel(Panel):
    bl_label = "My Panel"
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "BAMER"
      

    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.prop(mytool, "foo")
        
        layout.separator()
        
        
class CustomPanel(bpy.types.Panel):

    bl_label = "Blend_To_MER"
    bl_idname = "2"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "BAMER"

    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.operator(Blend_To_Json_Convertor.bl_idname,text="Convert!", icon='PLAY')


from bpy.utils import register_class,unregister_class

_classes =[Blend_To_Json_Convertor,
           CustomPanel,
           MyProperties,
           OBJECT_PT_CustomPanel,
]

def register():
    for cls in _classes:
        register_class(cls)
    bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)

def unregister():
    for cls in _classes:
        unregister_class(cls)
    del bpy.types.Scene.my_tool


if __name__ == "__main__":
    register()
