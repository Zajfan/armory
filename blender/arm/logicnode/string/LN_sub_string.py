from arm.logicnode.arm_nodes import *

class SubStringNode(ArmLogicTreeNode):
    """Use to get a part of a string."""
    bl_idname = 'LNSubStringNode'
    bl_label = 'Sub String'
    arm_version = 1

    def init(self, context):
        super(SubStringNode, self).init(context)
        self.add_input('NodeSocketString', 'String In')
        self.add_input('NodeSocketInt', 'Start')
        self.add_input('NodeSocketInt', 'End')
        self.add_output('NodeSocketString', 'String Out')

add_node(SubStringNode, category=PKG_AS_CATEGORY)
