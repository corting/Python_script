#-------------------------------------------------------------------------------
# Name:        entidad a multi entidad
# Purpose:     This Script make that a feature whit x row will make x features whit one row.
#El script realiza una operacion en la cual de una entidad con x registros se crean x entidades con un registro cada una.
#
# Author:      Felipe
#
# Created:     26/07/2016
# Copyright:   (c) Felipe 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy,time
START=time.clock()
wks=arcpy.env.workspace=r"C:\data"
arcpy.env.overwriteOutput = True
arcpy.CheckOutExtension("Spatial")
Entidad= # the path of your feature. La ruta de tu entidad
arcpy.MakeFeatureLayer_management(Entidad,"entidad_layer")
count=1
with arcpy.da.SearchCursor("entidad_layer", "OID@") as cursor:
    for row in cursor:
        print row[0]
        ide=row[0]
        sql="OBJECTID = " + str(ide)
        selec=arcpy.SelectLayerByAttribute_management("entidad_layer","NEW_SELECTION",sql)
        out= # the path of your feature. La ruta de tu entidad +str(ide)
        arcpy.CopyFeatures_management(selec, out)
        count=count+1
FIN=(time.clock()-START)
print "Script compelto. Tiempo de ejecucion {} segundos".format(FIN)