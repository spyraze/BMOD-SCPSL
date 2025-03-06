# To make this add-on installable, create an extension with it:
# https://docs.blender.org/manual/en/latest/advanced/extensions/getting_started.html
bl_info = {
        "name":"BAMER - Blender Addon for Map Editor Reborn for SCP:SL",
        "author":"Spyblaze",
        "version":"0.1",
        "blender":(4,3),
        "description":"Converts blender mesh into json file which can be used to make objects for server easily"
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
        

        def start():
            
            #tries to get if object has mesh
            try: 
                bpy.ops.object.mode_set(mode="OBJECT")
                has_mesh = True
                
            except:
                has_mesh = False
                
            if has_mesh == True:
                
                #switches to edit mode and gets basic indinformation
                bpy.ops.object.mode_set(mode="OBJECT")
                bpy.ops.object.mode_set(mode="EDIT")
                obj = bpy.context.edit_object
                me = obj.data
                bm = bmesh.from_edit_mesh(me)
                bpy.ops.mesh.select_all(action='SELECT')
                
            else:
                
            #left for non-mesh objects
                print(1)
       #Defines variables for path,save, color, face verts and location of verts
        file_path = Path(bpy.context.scene.my_tool.foo)
        path_to_file = pathlib.Path.home() / bpy.context.scene.my_tool.foo / "mesh.json"
        base_color=[]
        face_verts=[]
        vert_coords = []
        
        #makes vert faces
        def get_vert_face(face_verts,poloha_objekt,rotation,scale):
            #tries if object has mesh
            try:
                obj = bpy.context.edit_object
                me = obj.data
                bm = bmesh.from_edit_mesh(me)
                has_mesh= True
            except:
                has_mesh= False
                face_verts.append(1)
            
            #tries if object is not a cube
                
            if has_mesh== True and len(bm.faces) != 6 :
                
                
                for face in bm.faces:
                    face_to_verts=[]
                    for vert in face.verts:
                        face_to_verts.append(vert.index)
                    face_verts.append(face_to_verts)
                    
            if has_mesh == True and len(bm.faces) == 6 :
                bpy.ops.object.mode_set(mode="OBJECT")
                poloha_objekt.append(list(list(obj.location)))
                scale.append(list(list(obj.scale)))
                
                
                face_verts.append(1)
                
                rot3_axis = list(obj.rotation_euler)
                a=[0,0,0]
                rotation.append(a)
                for i in range(3):
                    rotation[0][i]=(rot3_axis[i]*180/3.14)
                    rotation[0][i]=round(rotation[0][i],1)
             
                
            else:
                print(1)
            
        #zisti polohu verts
        def get_coords(vert_coords): 
            
            a=0
            b=0
            
            try:
                obj = bpy.context.edit_object
                me = obj.data
                bm = bmesh.from_edit_mesh(me)
                for v in bm.verts:
                    if (v.select == True):  
                        obMat = obj.matrix_world  
                        vert_coords.append(list(obMat @ v.co))
                        for i in range(3):
                            vert_coords[a][b]=round(vert_coords[a][b],4)
                            b+=1
                        b=0
                        a+=1
            except:
                print(1)
        #zisti polohu kazdeho quadu
        poloha_objekt=[]
        def ziskaj_polohu(face_verts,vert_coords,poloha_objekt):
            #premmene
           
            try:
                poloha=[]
                pos=[]
                a=0
                b=0
                c=0
                x=0
                y=0
                z=0
                #pocet faces tolko krat to urobi

                for i in face_verts:
              #zopakovat 3-krat a ziskat x,y,z poloh*

                    for i in range(3):
                #ziska pozicie face x,y alebo z
                        for i in face_verts[a]:
                            c=face_verts[a][b]
                            pos.append(vert_coords[c][x])
                            b+=1  
                        for i in pos:
                            z+=pos[y]
                            y+=1  
                        pos=[]
                        z/=y
                        b=0
                        y=0    
                        x+=1
                        poloha.append(z)
                        z=0
                    x=0
                    a+=1
            #poloha objektov  
                    poloha_objekt.append(poloha)
                    poloha=[]
            except:
                a=[1,1,1]
                poloha_objekt.append(a)
        scale=[]        
        def get_scale(face_verts,vert_coords,poloha_objekt,scale,rotation):
            try:
                a=0
                b=0
                c=[]
                d=[]
                edges=[]
                for i in face_verts:
                    for i in range(2):
                        c.append(face_verts[b][a])
                        a+=1
                    a=1
                    d.append(c)
                    c=[]
                    for i in range(2):
                        c.append(face_verts[b][a])
                        a+=1
                    d.append(c)
                    edges.append(d)
                    d=[]
                    c=[]
                    a=0
                    b+=1
               
                b=0
                e=0
                f=0
                g=0
               
                print("")
                for i in face_verts:
                    for i in range(2):
                        a=edges[f][e][0]
                        b=edges[f][e][1]
                        c= (vert_coords[a][0]-vert_coords[b][0])**2 + (vert_coords[a][1]-vert_coords[b][1])**2 + (vert_coords[a][2]-vert_coords[b][2])**2
                        c = math.sqrt(c)
                        c = round(c,5)
                        e+=1
                        d.append(c)
                        c=[]
                       
                           
                    d.append(1.0)   
                    scale.append(d)
                   
                    g=0
                    d=[]
                    f+=1
                    e=0
                h=0
                f=0
                for i in face_verts:
                    for i in range(2):
                        a=edges[f][e][0]
                        b=edges[f][e][1]
                        for i in range(3):
                            if vert_coords[a][h] != vert_coords[b][h]:
                                if h == 0:
                                    c.append("x")
                                if h == 1:
                                    c.append("y")
                                if h == 2:
                                    c.append("z")
                                break
                            h+=1
                        h=0
                        e+=1
                    
                    if c[0] != "x" and c[1] == "x" or c[0] == "z" and c[1] == "y":
                        rotation[f][1]=90
                        
                    if c[0] != "y" and c[1] != "y" :
                        
                        rotation[f][2]+=180
                    
                    
                    
                    
                    c=[]
                    f+=1
                    e=0
                
                
                rotation =[]
                
            except:
                a=[1,1,1]
                scale.append(a)
        def get_color(base_color):
            try:
                obj = bpy.context.edit_object
                me = obj.data
                bm = bmesh.from_edit_mesh(me)
           
        # Check if the object has mesh data
                try:
                    if obj.type == 'MESH':
                    # Get the mesh data
                        mesh = obj.data
                   
                    # Loop through the faces
                        for face in mesh.polygons:
                        # Get the material index for the face
                            mat_index = face.material_index

                        # Check if the material index is valid
                           
                            material = obj.data.materials[0]



                            if material.use_nodes:
                            # Find the Principled BSDF node
                                for node in material.node_tree.nodes:
                                    if node.type == 'BSDF_PRINCIPLED':
                                    # Get the base color
                                        color = node.inputs['Base Color'].default_value
                                        color = '#%02x%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(color[3] * 255))
                                        base_color.append(str(color))
                                        color=[]
                                        
                except:
                    a=["ccccccff"]
                    base_color.append(a)
            except:
                a=["ccccccff"]
                base_color.append(a)
        def get_rotation(rotation):
            try:
                scene = bpy.context.scene
                obj = bpy.context.edit_object
                me = obj.data
                bm = bmesh.from_edit_mesh(me)
                mesh = obj.data
                
               
                # Loop through the faces and get their normals and rotations
                for face in mesh.polygons:
                    normal = face.normal
                    rotation_uwu = normal.to_track_quat('Y', 'Z').to_euler()  # Convert normal to rotation
                    rotation_degrees = [math.degrees(angle) for angle in rotation_uwu]
                    rotation.append(rotation_degrees)
                a=0
                b=0
                for i in rotation:
                    for i in range(3):
                        rotation[a][b]=round(rotation[a][b],4)
                        if rotation[a][b] < 0:
                            rotation[a][b] = 360 + rotation[a][b]
                        if rotation[a][b] == 0.0:
                            rotation[a][b] = 0.0

                         
                        b+=1
                    
                    #if rotation[a][2] == 180 and poloha_objekt[a][1]!=0 or rotation[a][2] == 0 and poloha_objekt[a][1]!=0:
                        #rotation[a][2] =   rotation[a][2] - 180
                    b=0
                    a+=1
                
                
                a=0
            except:
                a=[0,0,0]
                rotation.append(a)  
           
        def get_json(number_of_quads,id_objekt,base_color,poloha_objekt,rotation,scale,face_verts):
            
            
            a=0
            id=random.randint(0,1000000)
            bpy.ops.object.mode_set(mode="OBJECT")
            bpy.ops.object.mode_set(mode="EDIT")
            obj = bpy.context.edit_object
            me = obj.data
            bm = bmesh.from_edit_mesh(me)
            if len(bm.faces)==6:
                primitive_type=3
                rotation[0][0]=rotation[0][0]*(-1)
            if len(bm.faces)!=6:
                primitive_type=5
                
            if  len(bm.faces) == 34:
                face_verts=[]
                scale=[]
                poloha_objekt=[]
                rotation=[]
                bpy.ops.object.mode_set(mode="OBJECT")
                poloha_objekt.append(list(list(obj.location)))
                scale.append(list(list(obj.scale)))
                scale[0][1]=scale[0][1]/2
                primitive_type=2
                face_verts.append(1)
                
                rot3_axis = list(obj.rotation_euler)
                a=[0,0,0]
                rotation.append(a)
                for i in range(3):
                    rotation[0][i]=(rot3_axis[i]*180/3.14)
                    rotation[0][i]=round(rotation[0][i],1)
                    color=list(obj.color)
                    color = '#%02x%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(color[3] * 255))
                    base_color.append(str(color))
                    color=[]
                rotation[0][0]=rotation[0][0]*(-1)
             
            a=0  
            if  len(bm.faces) == 512:
                face_verts=[]
                scale=[]
                poloha_objekt=[]
                rotation=[]
                bpy.ops.object.mode_set(mode="OBJECT")
                poloha_objekt.append(list(list(obj.location)))
                scale.append(list(list(obj.scale)))
                
                primitive_type=0
                face_verts.append(1)
                
                
                a=[0,0,0]
                rotation.append(a)
                
                color=list(obj.color)
                color = '#%02x%02x%02x%02x' % (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255), int(color[3] * 255))
                base_color.append(str(color))
                color=[]
                
             
            a=0  
            for i in face_verts:
               
                
                data1={}
                data1={
                    "Name": str(id),
                    "ObjectId": id,
                    "ParentId":  23126,
                    "Position":{
                        "x": poloha_objekt[a][0],
                        "y":poloha_objekt[a][2],
                        "z":poloha_objekt[a][1]
                    },
                    "Rotation":{
                        "x": rotation[a][0],
                        "y": rotation[a][2],
                        "z": rotation[a][1]
                    },
                    "Scale":{
                        "x": scale[a][0],
                        "y": scale[a][1],
                        "z": scale[a][2]
                    },
                    "BlockType": 1,
                    "Properties": {
                    "PrimitiveType": primitive_type,
                    "Color": base_color[a],
                    "PrimitiveFlags": 3
                    }
                }
                a+=1
                id-=1
                
                blocks.append(data1)
                
            number_of_quads=a
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
               
        def Main(number_of_quads,blocks,base_color,rotation,scale,poloha_objekt,face_verts,vert_coords,object_position):
            start()
            get_color(base_color)
            
            get_vert_face(face_verts,poloha_objekt,rotation,scale)
            
            get_coords(vert_coords)
            
            ziskaj_polohu(face_verts,vert_coords,poloha_objekt)
            
            get_rotation(rotation)
            get_scale(face_verts,vert_coords,poloha_objekt,scale,rotation)
            
            get_json(number_of_quads,id_objekt,base_color,poloha_objekt,rotation,scale,face_verts)
            
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
                object_position=obj.location
                base_color=[]
                rotation =[]  
                scale=[]
                poloha_objekt=[]
                face_verts=[]
                vert_coords = []
                primitive_type=[]
                Main(number_of_quads,blocks,base_color,rotation,scale,poloha_objekt,face_verts,vert_coords,object_position)

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
