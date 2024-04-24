# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def ZUHUI_417(fileplace,chang,kuan,gao,jiaodux,jiaoduy,jiaoduz,GriRadius,GriDepth,RotSpeed,GriSpeed,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10):
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    catia = mdb.openCatia(fileName=fileplace,
        topology=SOLID, useServer=True)
    mdb.models['Model_240417'].PartFromGeometryFile(name='DaMoDrill', 
        geometryFile=catia, combine=False, dimensionality=THREE_D, 
        type=DEFORMABLE_BODY, scale=1.0)
    p = mdb.models['Model_240417'].parts['DaMoDrill']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    s = mdb.models['Model_240417'].ConstrainedSketch(name='__profile__', 
        sheetSize=200.0)
    g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
    s.setPrimaryObject(option=STANDALONE)
    s.rectangle(point1=(0.0, 0.0), point2=(40.0, 30.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=162.287, 
        farPlane=214.837, width=191.351, height=84.278, cameraPosition=(
        9.15305, 8.19067, 188.562), cameraTarget=(9.15305, 8.19067, 0))
    s.ObliqueDimension(vertex1=v[1], vertex2=v[2], textPoint=(8.42588901519775, 
        35.9194564819336), value=40.0)
    s.ObliqueDimension(vertex1=v[2], vertex2=v[3], textPoint=(48.1293640136719, 
        15.2502307891846), value=30.0)
    s=mdb.models['Model_240417'].sketches['__profile__']
    s.Parameter(name='CHANG', path='dimensions[0]', expression=chang)
    s.Parameter(name='KUAN', path='dimensions[1]', expression=kuan,
        previousParameter='CHANG')
    p = mdb.models['Model_240417'].Part(name='Part-DaMoBan', 
        dimensionality=THREE_D, type=DEFORMABLE_BODY)
    p = mdb.models['Model_240417'].parts['Part-DaMoBan']
    p.BaseSolidExtrude(sketch=s, depth=5.0)
    s.unsetPrimaryObject()
    p = mdb.models['Model_240417'].parts['Part-DaMoBan']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    del mdb.models['Model_240417'].sketches['__profile__']
    a = mdb.models['Model_240417'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Model_240417'].rootAssembly
    a.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['Model_240417'].parts['DaMoDrill']
    a.Instance(name='DaMoDrill-1', part=p, dependent=ON)
    p = mdb.models['Model_240417'].parts['Part-DaMoBan']
    a.Instance(name='Part-DaMoBan-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=941.573, 
        farPlane=1500.25, width=224.692, height=98.9628, viewOffsetX=7.59549, 
        viewOffsetY=173.081)
    a = mdb.models['Model_240417'].rootAssembly
    a.rotate(instanceList=('Part-DaMoBan-1', ), axisPoint=(40.0, 30.0, 5.0), 
        axisDirection=(-20.0, 0.0, 0.0), angle=90.0)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=585.885, 
        farPlane=1317.27, width=813.174, height=358.152, viewOffsetX=-33.1138, 
        viewOffsetY=192.872)
    a = mdb.models['Model_240417'].rootAssembly
    a.translate(instanceList=('DaMoDrill-1', ), vector=(-80.0, 541.0, 5.0))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=669.869, 
        farPlane=1233.29, width=113.425, height=49.9566, viewOffsetX=5.27434, 
        viewOffsetY=125.623)
    a = mdb.models['Model_240417'].rootAssembly
    a.rotate(instanceList=('DaMoDrill-1', ), axisPoint=(0.0, 0.0, 0.0), 
        axisDirection=(0.0, 0.0, 10.0), angle=jiaoduz)


