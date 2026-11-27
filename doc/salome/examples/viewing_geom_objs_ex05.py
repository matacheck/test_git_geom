# Changing Edges and Iso-lines Width

from salome.kernel import salome
salome.salome_init_without_session()
from salome.kernel import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()

box = geompy.MakeBox(0,0,0, 50,50,50)
edge = geompy.MakeLineTwoPnt(geompy.MakeVertex(0,0,60), geompy.MakeVertex(50,50,60))
box_id = geompy.addToStudy(box,"Box")
edge_id = geompy.addToStudy(edge,"Edge")

gg = salome.ImportComponentGUI("GEOM")
gg.createAndDisplayGO(box_id)
gg.createAndDisplayGO(edge_id)
gg.setColor(edge_id,255,0,0)
gg.setEdgeWidth(edge_id,4)   # width of the edges (lines) of the presentation
gg.setIsosWidth(box_id,2)    # width of the iso-lines

# default widths for newly displayed objects are set in the preferences:
# Geometry > General > Edges width / Isolines width
