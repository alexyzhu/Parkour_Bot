OBS_SIZE = 6
SIZE = 30
MAX_EPISODE_STEPS = 50
MAX_GLOBAL_STEPS = 10000
EPSILON_DECAY = .995
MIN_EPSILON = .05
ACTION_DICT = {
    0: 'move 1',  # Move forward at normal speed
    1: 'move 0',  # Stop moving
    2: 'turn -0.5',  # Turn to the left
    3: 'turn 0.5', # turn to the right
    4: 'turn 0' # stop turning
    5: 'jump 1'  # start jumping
    6: 'jump 0' # stop jumping
}


def GetMissionXML():
    return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

                <About>
                    <Summary>Diamond Collector</Summary>
                </About>

                <ServerSection>
                    <ServerInitialConditions>
                        <Time>
                            <StartTime>12000</StartTime>
                            <AllowPassageOfTime>true</AllowPassageOfTime>
                        </Time>
                        <Weather>clear</Weather>
                    </ServerInitialConditions>
                    <ServerHandlers>
                        <FlatWorldGenerator generatorString="3;7,2;1;"/>
                        <DrawingDecorator>''' + \
                            "<DrawCuboid x1='{}' x2='{}' y1='2' y2='2' z1='{}' z2='{}' type='air'/>".format(-SIZE, SIZE, -SIZE, SIZE) + \
                            "<DrawCuboid x1='{}' x2='{}' y1='1' y2='1' z1='{}' z2='{}' type='grass_block'/>".format(-SIZE, SIZE, -SIZE, SIZE) + \
                            drawPath() + \
                            '''<DrawBlock x='0'  y='2' z='0' type='air' />
                            <DrawBlock x='0'  y='1' z='0' type='diamond_block' />
                        </DrawingDecorator>
                        <ServerQuitWhenAnyAgentFinishes/>
                    </ServerHandlers>
                </ServerSection>

                <AgentSection mode="Survival">
                    <Name>CS175DiamondCollector</Name>
                    <AgentStart>
                        <Placement x="0.5" y="2" z="0.5" pitch="45" yaw="0"/>
                        <Inventory>
                            <InventoryItem slot="0" type="diamond_pickaxe"/>
                        </Inventory>
                    </AgentStart>
                    <AgentHandlers>
                        <ContinuousMovementCommands/>
                        <ObservationFromFullStats/>
                        <ObservationFromGrid>
                            <Grid name="floorAll">
                                <min x="-'''+str(int(OBS_SIZE/2))+'''" y="-1" z="-'''+str(int(OBS_SIZE/2))+'''"/>
                                <max x="'''+str(int(OBS_SIZE/2))+'''" y="1" z="'''+str(int(OBS_SIZE/2))+'''"/>
                            </Grid>
                        </ObservationFromGrid>
                        <RewardForTouchingBlockType>
                            <Block reward="10" type="gold_block"/>
                        </RewardForTouchingBlockType>
                        <RewardForTouchingBlockType>
                            <Block reward="1" type="diamond_block"/>
                        </RewardForTouchingBlockType>
                        <RewardForTouchingBlockType>
                            <Block reward="-1" type="grass_block"/>
                        </RewardForTouchingBlockType>
                        <AgentQuitFromReachingCommandQuota total="'''+str(MAX_EPISODE_STEPS)+'''" />
                    </AgentHandlers>
                </AgentSection>
            </Mission>'''

def drawPath():
    path = ""
    for i in range(10):
        path += f"<DrawBlock x='0'  y='1' z='{i}' type='diamond_block' />"
    path += "<DrawBlock x='0'  y='1' z='10' type='gold_block' />"
    return path
