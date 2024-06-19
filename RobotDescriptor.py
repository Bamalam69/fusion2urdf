#Author-syuntoku14
#Description-Generate URDF file from Fusion 360
from __future__ import annotations

import adsk, adsk.core, adsk.fusion, traceback
import os
import sys
from .lib.utils import log
# from .core import Link, Joint, Write

from .lib import RobotDescriber as rd

"""
# length unit is 'cm' and inertial unit is 'kg/cm^2'
# If there is no 'body' in the root component, maybe the corrdinates are wrong.
# TODO: wtf is he talking about?
"""

# joint effort: 100
# joint velocity: 100
# supports "Revolute", "Rigid" and "Slider" joint types

# I'm not sure how prismatic joint acts if there is no limit in fusion model

robotDescriber = rd.RobotDescriber()

def run(context):
    # ui = None
    # success_msg = 'Successfully create URDF file'
    # msg = success_msg
    log("Started plugin")
    
    try:
        robotDescriber.setupUI()

        # ui = app.userInterface
        # product = app.activeProduct
        # design = adsk.fusion.Design.cast(product)
        # title = 'Fusion2URDF'
        # if not design:
        #     ui.messageBox('No active Fusion design', title)
        #     return

        # root = design.rootComponent  # root component
        # components = design.allComponents

        # # TODO: Show a dialog asking for what to name it...
        # # set the names
        
        # robot_name = root.name.split()[0]
        # package_name = robot_name + '_description'
        # save_dir = utils.file_dialog(ui)
        # if not save_dir:
        #     ui.messageBox('Conversion was canceled', title)
        #     return 0
        
        # save_dir = save_dir + '/' + package_name
        # try: os.mkdir(save_dir)
        # except:
        #     pass

        # package_dir = os.path.abspath(os.path.dirname(__file__)) + '/package/'
        
        # --------------------
        # set dictionaries
        
        # Generate joints_dict. All joints are related to root.
        # joints_dict, msg = Joint.make_joints_dict(root, msg)
        # if msg != success_msg:
        #     ui.messageBox(msg, title)
        #     return 0
        
        # # Generate inertial_dict
        # inertial_dict, msg = Link.make_inertial_dict(root, msg)
        # if msg != success_msg:
        #     ui.messageBox(msg, title)
        #     return 0
        # elif not 'base_link' in inertial_dict:
        #     msg = 'There is no base_link. Please set base_link and run again.'
        #     ui.messageBox(msg, title)
        #     return 0
        
        # links_xyz_dict = {}
        
        # # --------------------
        # # Generate URDF
        # Write.write_urdf(joints_dict, links_xyz_dict, inertial_dict, package_name, robot_name, save_dir)
        # Write.write_materials_xacro(joints_dict, links_xyz_dict, inertial_dict, package_name, robot_name, save_dir)
        # Write.write_transmissions_xacro(joints_dict, links_xyz_dict, inertial_dict, package_name, robot_name, save_dir)
        # Write.write_gazebo_xacro(joints_dict, links_xyz_dict, inertial_dict, package_name, robot_name, save_dir)
        # Write.write_display_launch(package_name, robot_name, save_dir)
        # Write.write_gazebo_launch(package_name, robot_name, save_dir)
        # Write.write_control_launch(package_name, robot_name, save_dir, joints_dict)
        # Write.write_yaml(package_name, robot_name, save_dir, joints_dict)
        
        # # copy over package files
        # utils.copy_package(save_dir, package_dir)
        # utils.update_cmakelists(save_dir, package_name)
        # utils.update_package_xml(save_dir, package_name)

        # # Generate STl files        
        # utils.copy_occs(root)
        # utils.export_stl(design, save_dir, components)   
        
        # ui.messageBox(msg, title)
        
    except:
        log('Failed:\n{}'.format(traceback.format_exc()))
        # if ui:
        #     ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def stop(context):
    log('Stopping')

    # Remove the ui stuff
    robotDescriber.teardownUI()
    