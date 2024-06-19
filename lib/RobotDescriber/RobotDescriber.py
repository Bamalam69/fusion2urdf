from __future__ import annotations
from ..utils import log
import adsk.core as adcore

class DescribeCommandExecuteHandler(adcore.CommandEventHandler):
    def __init__(self, robotDescriber: RobotDescriber):
        super().__init__()
        self.robotDescriber = robotDescriber

    def notify(self, args):
        log("DescribeCommandExecuteHandler notify")
        try:
            self.onExecute(args)
        except Exception as e:
            log("Error in DescribeCommandExecuteHandler: {}".format(e))

    def onExecute(self, args):
        log("DescribeCommandExecuteHandler onExecute")
        self.robotDescriber.describe()

# For a button to be added to the UI, it needs to be added to the command definitions.
class DescribeCommandHandler(adcore.CommandCreatedEventHandler):
    def __init__(self, robotDescriber: RobotDescriber):
        super().__init__()
        self.robotDescriber = robotDescriber
        log("DescribeCommandHandler init")

    def notify(self, args):
        log("DescribeCommandHandler notify")

        # Add the actual execute callback:
        args.command.execute.add(DescribeCommandExecuteHandler(self.robotDescriber))

### Intended to be the main entry point for all URDF generation.
class RobotDescriber:
    buttonID = 'robotdescriber'
    addInTabID = 'robotdescriberTab'
    addIngPanelID = 'RobotDescriberPanel'

    def setupUI(self):
        log("RobotDescriber setupUI")

        # Add a command that will be displayed in the panel.
        ui = adcore.Application.get().userInterface
        cmdDefs = ui.commandDefinitions

        # Check if cmd def already exists:
        cmdDef = cmdDefs.itemById(RobotDescriber.buttonID)
        if cmdDef:
            cmdDef.deleteMe()

        cmdDef = cmdDefs.addButtonDefinition(
            RobotDescriber.buttonID,
            'Describe Robot',
            'Generate URDF file from Fusion 360',
            'Resources/SampleCmdColor'
        )
        
        cmdDef.commandCreated.add(DescribeCommandHandler(self))

        # Get the workspace
        workspaces = ui.workspaces
        workspace = workspaces.itemById('FusionSolidEnvironment')

        # Add tab to the workspace
        customTab = workspace.toolbarTabs.itemById(RobotDescriber.addInTabID)
        if customTab:
            customTab.deleteMe()
        customTab = workspace.toolbarTabs.add(RobotDescriber.addInTabID, 'RobotDescriber')

        # Add panel to the tab
        panel = customTab.toolbarPanels.itemById(RobotDescriber.addIngPanelID)
        if panel:
            panel.deleteMe()
        panel = customTab.toolbarPanels.add(RobotDescriber.addIngPanelID, 'RobotDescriber Panel', 'RobotDescriberPanel', False)

        # Add the command to the panel
        buttonControl = panel.controls.addCommand(cmdDef)
        buttonControl.isPromoted = True

        log("Added button to UI")

    def teardownUI(self):
        log("RobotDescriber teardownUI")
        self.ui.commandDefinitions.itemById(RobotDescriber.buttonID).deleteMe()

    def describe(self):
        log("RobotDescriber describe")