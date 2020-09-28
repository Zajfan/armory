from arm.logicnode.arm_nodes import *

class GetDistanceNode(ArmLogicTreeNode):
    """Get the euclidian distance between the two given objects.

    @see For distance between two locations, use the `Distance` operator
        in the *[`Vector Math`](#vector-math)* node."""
    bl_idname = 'LNGetDistanceNode'
    bl_label = 'Get Distance'
    arm_version = 1

    def init(self, context):
        super(GetDistanceNode, self).init(context)
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_output('NodeSocketFloat', 'Distance')

add_node(GetDistanceNode, category=PKG_AS_CATEGORY)
