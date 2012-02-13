"""

"""

# <pep8-80 compliant>

bl_info = {
    "name": "ManuScrib",
    "author": "Pierre-Maël Crétinon (pima)",
    "version": (0, 0, 5),
    "blender": (2, 6, 2),
    "location": "Properties > Object data > ManuScrib panel",
    "description": "Modify selected curve Text content",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"}

import bpy


class ManuScribPanel(bpy.types.Panel):
    bl_label = "ManuScrib"
    bl_idname = "OBJECT_PT_text"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"

    def draw(self, context):
        layout = self.layout
        obj = context.object
        row = layout.row()
#       read/write obj.data.body from an input text box
        row.prop(obj.data, "body")


def register():
    bpy.utils.register_class(ManuScribPanel)


def unregister():
    bpy.utils.unregister_class(ManuScribPanel)


if __name__ == "__main__":
    register()


"""
copyleft: Copyright 2012 Pierre-Maël Crétinon
licence: GPLv3+

***** BEGIN GPL LICENSE BLOCK *****
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
***** END GPL LICENSE BLOCK *****
"""
