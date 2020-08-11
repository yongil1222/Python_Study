from datetime import datetime

def make_kml_header(KML_file, filename):
    KML_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    KML_file.write(' <kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">\n')
    KML_file.write('<Document>\n')
    KML_file.write('\t<name>' + filename + '</name>\n')
    KML_file.write('\t\t<StyleMap id="Aiding">\n')
    KML_file.write('\t\t\t<Pair>\n')
    KML_file.write('\t\t\t\t<key>normal</key>\n')
    KML_file.write('\t\t\t\t<Style>\n')
    KML_file.write('\t\t\t\t\t<IconStyle>\n')
    KML_file.write('\t\t\t\t\t\t<color>FF00FFFF</color>\n')
    KML_file.write('\t\t\t\t\t\t<scale>0.5</scale>\n')
    KML_file.write('\t\t\t\t\t\t<Icon>\n')
    KML_file.write('\t\t\t\t\t\t\t<href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href>\n')
    KML_file.write('\t\t\t\t\t\t</Icon>\n')
    KML_file.write('\t\t\t\t\t</IconStyle>\n')
    KML_file.write('\t\t\t\t\t<LabelStyle>\n')
    KML_file.write('\t\t\t\t\t\t<scale>0</scale>\n')
    KML_file.write('\t\t\t\t\t</LabelStyle>\n')
    KML_file.write('\t\t\t\t</Style>\n')
    KML_file.write('\t\t\t</Pair>\n')
    KML_file.write('\t\t\t<Pair>\n')
    KML_file.write('\t\t\t\t<key>highlight</key>\n')
    KML_file.write('\t\t\t\t<Style>\n')
    KML_file.write('\t\t\t\t\t<IconStyle>\n')
    KML_file.write('\t\t\t\t\t\t<color>FFFFFFFF</color>\n')
    KML_file.write('\t\t\t\t\t\t<scale>0.7</scale>\n')
    KML_file.write('\t\t\t\t\t\t<Icon>\n')
    KML_file.write('\t\t\t\t\t\t\t<href>http://maps.google.com/mapfiles/kml/shapes/road_shield3.png</href>\n')
    KML_file.write('\t\t\t\t\t\t</Icon>\n')
    KML_file.write('\t\t\t\t\t</IconStyle>\n')
    KML_file.write('\t\t\t\t\t<LabelStyle>\n')
    KML_file.write('\t\t\t\t\t\t<scale>0</scale>\n')
    KML_file.write('\t\t\t\t\t</LabelStyle>\n')
    KML_file.write('\t\t\t\t</Style>\n')
    KML_file.write('\t\t\t</Pair>\n')
    KML_file.write('\t\t</StyleMap>\n')
    for degree in range(360):
        KML_file.write('\t\t<StyleMap id="Aiding' + str(degree) + '">\n')
        KML_file.write('\t\t\t<Pair>\n')
        KML_file.write('\t\t\t\t<key>normal</key>\n')
        KML_file.write('\t\t\t\t<Style>\n')
        KML_file.write('\t\t\t\t\t<IconStyle>\n')
        KML_file.write('\t\t\t\t\t\t<color>FF00FFFF</color>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0.5</scale>\n')
        KML_file.write('\t\t\t\t\t\t<Icon>\n')
        KML_file.write('\t\t\t\t\t\t\t<href>http://www.earthpoint.us/Dots/GoogleEarth/WhiteShapes/arrow.png</href>\n')
        KML_file.write('\t\t\t\t\t\t</Icon>\n')
        KML_file.write('\t\t\t\t\t\t<heading>' + str((degree+180)%360) + '</heading>\n')
        KML_file.write('\t\t\t\t\t</IconStyle>\n')
        KML_file.write('\t\t\t\t\t<LabelStyle>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0</scale>\n')
        KML_file.write('\t\t\t\t\t</LabelStyle>\n')
        KML_file.write('\t\t\t\t</Style>\n')
        KML_file.write('\t\t\t</Pair>\n')
        KML_file.write('\t\t\t<Pair>\n')
        KML_file.write('\t\t\t\t<key>highlight</key>\n')
        KML_file.write('\t\t\t\t<Style>\n')
        KML_file.write('\t\t\t\t\t<IconStyle>\n')
        KML_file.write('\t\t\t\t\t\t<color>FFFFFFFF</color>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0.7</scale>\n')
        KML_file.write('\t\t\t\t\t\t<Icon>\n')
        KML_file.write('\t\t\t\t\t\t\t<href>http://www.earthpoint.us/Dots/GoogleEarth/WhiteShapes/arrow.png</href>\n')
        KML_file.write('\t\t\t\t\t\t</Icon>\n')
        KML_file.write('\t\t\t\t\t\t<heading>' + str((degree+180)%360) + '</heading>\n')
        KML_file.write('\t\t\t\t\t</IconStyle>\n')
        KML_file.write('\t\t\t\t\t<LabelStyle>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0</scale>\n')
        KML_file.write('\t\t\t\t\t</LabelStyle>\n')
        KML_file.write('\t\t\t\t</Style>\n')
        KML_file.write('\t\t\t</Pair>\n')
        KML_file.write('\t\t</StyleMap>\n')
    for degree in range(360):
        KML_file.write('\t\t<StyleMap id="MMF-0-Aiding' + str(degree) + '">\n')
        KML_file.write('\t\t\t<Pair>\n')
        KML_file.write('\t\t\t\t<key>normal</key>\n')
        KML_file.write('\t\t\t\t<Style>\n')
        KML_file.write('\t\t\t\t\t<IconStyle>\n')
        KML_file.write('\t\t\t\t\t\t<color>FFFF0000</color>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0.5</scale>\n')
        KML_file.write('\t\t\t\t\t\t<Icon>\n')
        KML_file.write('\t\t\t\t\t\t\t<href>http://www.earthpoint.us/Dots/GoogleEarth/WhiteShapes/arrow.png</href>\n')
        KML_file.write('\t\t\t\t\t\t</Icon>\n')
        KML_file.write('\t\t\t\t\t\t<heading>' + str((degree+180)%360) + '</heading>\n')
        KML_file.write('\t\t\t\t\t</IconStyle>\n')
        KML_file.write('\t\t\t\t\t<LabelStyle>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0</scale>\n')
        KML_file.write('\t\t\t\t\t</LabelStyle>\n')
        KML_file.write('\t\t\t\t</Style>\n')
        KML_file.write('\t\t\t</Pair>\n')
        KML_file.write('\t\t\t<Pair>\n')
        KML_file.write('\t\t\t\t<key>highlight</key>\n')
        KML_file.write('\t\t\t\t<Style>\n')
        KML_file.write('\t\t\t\t\t<IconStyle>\n')
        KML_file.write('\t\t\t\t\t\t<color>FFFFFFFF</color>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0.7</scale>\n')
        KML_file.write('\t\t\t\t\t\t<Icon>\n')
        KML_file.write('\t\t\t\t\t\t\t<href>http://www.earthpoint.us/Dots/GoogleEarth/WhiteShapes/arrow.png</href>\n')
        KML_file.write('\t\t\t\t\t\t</Icon>\n')
        KML_file.write('\t\t\t\t\t\t<heading>' + str((degree+180)%360) + '</heading>\n')
        KML_file.write('\t\t\t\t\t</IconStyle>\n')
        KML_file.write('\t\t\t\t\t<LabelStyle>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0</scale>\n')
        KML_file.write('\t\t\t\t\t</LabelStyle>\n')
        KML_file.write('\t\t\t\t</Style>\n')
        KML_file.write('\t\t\t</Pair>\n')
        KML_file.write('\t\t</StyleMap>\n')
    for degree in range(360):
        KML_file.write('\t\t<StyleMap id="MMF-1-Aiding' + str(degree) + '">\n')
        KML_file.write('\t\t\t<Pair>\n')
        KML_file.write('\t\t\t\t<key>normal</key>\n')
        KML_file.write('\t\t\t\t<Style>\n')
        KML_file.write('\t\t\t\t\t<IconStyle>\n')
        KML_file.write('\t\t\t\t\t\t<color>FFFFFF00</color>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0.5</scale>\n')
        KML_file.write('\t\t\t\t\t\t<Icon>\n')
        KML_file.write('\t\t\t\t\t\t\t<href>http://www.earthpoint.us/Dots/GoogleEarth/WhiteShapes/arrow.png</href>\n')
        KML_file.write('\t\t\t\t\t\t</Icon>\n')
        KML_file.write('\t\t\t\t\t\t<heading>' + str((degree+180)%360) + '</heading>\n')
        KML_file.write('\t\t\t\t\t</IconStyle>\n')
        KML_file.write('\t\t\t\t\t<LabelStyle>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0</scale>\n')
        KML_file.write('\t\t\t\t\t</LabelStyle>\n')
        KML_file.write('\t\t\t\t</Style>\n')
        KML_file.write('\t\t\t</Pair>\n')
        KML_file.write('\t\t\t<Pair>\n')
        KML_file.write('\t\t\t\t<key>highlight</key>\n')
        KML_file.write('\t\t\t\t<Style>\n')
        KML_file.write('\t\t\t\t\t<IconStyle>\n')
        KML_file.write('\t\t\t\t\t\t<color>FFFFFFFF</color>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0.7</scale>\n')
        KML_file.write('\t\t\t\t\t\t<Icon>\n')
        KML_file.write('\t\t\t\t\t\t\t<href>http://www.earthpoint.us/Dots/GoogleEarth/WhiteShapes/arrow.png</href>\n')
        KML_file.write('\t\t\t\t\t\t</Icon>\n')
        KML_file.write('\t\t\t\t\t\t<heading>' + str((degree+180)%360) + '</heading>\n')
        KML_file.write('\t\t\t\t\t</IconStyle>\n')
        KML_file.write('\t\t\t\t\t<LabelStyle>\n')
        KML_file.write('\t\t\t\t\t\t<scale>0</scale>\n')
        KML_file.write('\t\t\t\t\t</LabelStyle>\n')
        KML_file.write('\t\t\t\t</Style>\n')
        KML_file.write('\t\t\t</Pair>\n')
        KML_file.write('\t\t</StyleMap>\n\n\n')

def make_kml_tail(KML_file):
    KML_file.write('\t</Document>\n')
    KML_file.write('</kml>')		

def open_Position_folder(KML_file):
    KML_file.write('\t\t<Folder>\n')
    KML_file.write('\t\t\t<name>Position</name>\n')
    KML_file.write('\t\t\t<open>1</open>\n')

def open_AOSP_folder(KML_file):
    KML_file.write('\t\t\t<Folder id="AOSP">\n')
    KML_file.write('\t\t\t\t<name>AOSP Location</name>\n')

def open_MMF_folder(KML_file):
    KML_file.write('\t\t\t<Folder id="MMF">\n')
    KML_file.write('\t\t\t\t<name>MMF Location</name>\n')

def open_Track_folder(KML_file):
    KML_file.write('\t\t<Folder id="Track AOSP">\n')
    KML_file.write('\t\t\t<name>Track AOSP</name>\n')
    KML_file.write('\t\t\t<Placemark>')
    KML_file.write('\t\t\t\t<visibility>0</visibility>\n')
    KML_file.write('\t\t\t\t<open>0</open>\n')
    KML_file.write('\t\t\t\t<Style>\n\t\t\t\t\t<LineStyle>\n\t\t\t\t\t\t<color>ffffffff</color>\n\t\t\t\t\t\t<width>3</width>\n\t\t\t\t\t</LineStyle>\n\t\t\t\t</Style>\n')
    KML_file.write('\t\t\t\t<LineString>\n\t\t\t\t\t<coordinates>\n')

def close_Position_folder(KML_file):
    KML_file.write('\t\t</Folder>\n')

def close_AOSP_folder(KML_file):
    KML_file.write('\t\t\t</Folder>\n')

def close_MMF_folder(KML_file):
    KML_file.write('\t\t\t</Folder>\n')

def close_Track_folder(KML_file):
    KML_file.write('\n\t\t\t\t\t</coordinates>\n\t\t\t\t</LineString>\n\t\t\t</Placemark>\n')
    KML_file.write('\t\t</Folder>\n')

def add_AOSP_location(lines, logFileName, KML_file):
    for line in lines:
        splitted = line.split(' ')
        if 'handleMessage(REPORT_LOCATION,' in splitted:
            s_idx = splitted.index('Location[gps')
            l_time = splitted[1]
            l_location = splitted[s_idx+1].split(',')
            if float(l_location[0]) == 0.0 and float(l_location[1]) == 0.0 :
                continue
            for temp in splitted:
                items = temp.split('=')
                if 'hAcc' in items:
                    hAcc = items[1]
                elif 'vAcc' in items:
                    vAcc = items[1]
                elif 'alt' in items:
                    alt = items[1]
                elif 'vel' in items:
                    vel = items[1]
                elif 'bear' in items:
                    bear = items[1]
                elif '{Bundle[{satellites' in items:
                    satellites = items[1].replace(",","")
                elif 'maxCn0' in items:
                    maxCn0 = items[1].replace(",","")
                elif 'meanCn0' in items:
                    meanCn0 = items[1].replace("}]}])\n","")
            KML_file.write('\t\t\t\t<Placemark>\n')
            KML_file.write('\t\t\t\t\t<name>' + l_time + '</name>\n')
            KML_file.write('\t\t\t\t\t<description>\n')
            KML_file.write('\t\t\t\t\t\t<![CDATA[<b>AOSP Position</b><br> FileName: '+ logFileName + '<br> LogTime: ' + splitted[0] + ' ' + l_time + '<br>')
            KML_file.write(' Latitude: ' + l_location[0] + '<br> Longitude: ' + l_location[1])
            if 'alt' in locals():
                KML_file.write('<br> Altitude: ' + alt)
            if 'vel' in locals():
                KML_file.write('<br> Speed: ' + vel)
                del(vel)
            if 'bear'in locals():
                KML_file.write('<br> Heading: ' + bear)
            if 'hAcc' in locals():
                KML_file.write('<br> hAcc: ' + hAcc)
                del(hAcc)
            if 'vAcc' in locals():
                KML_file.write('<br> vAcc: ' + vAcc)
                del(vAcc)
            if 'satellites' in locals():
                KML_file.write('<br> Satellites: ' + satellites)
                del(satellites)
            if 'maxCn0' in locals():
                KML_file.write('<br> maxCn0: ' + maxCn0)
                del(maxCn0)
            if 'meanCn0' in locals():
                KML_file.write('<br> meanCn0: ' + meanCn0)
                del(meanCn0)
            KML_file.write(']]>\n')
            KML_file.write('\t\t\t\t\t</description>\n')
            KML_file.write('\t\t\t\t\t<styleUrl>Aiding')
            if 'bear' in locals():
                KML_file.write(bear.split('.')[0])
                del(bear)
            KML_file.write('</styleUrl>\n')
            KML_file.write('\t\t\t\t\t<TimeStamp>\n')
            KML_file.write('\t\t\t\t\t\t<when>' + str(datetime.today().year) + '-' + splitted[0] + 'T' + l_time.split('.')[0] + '</when>\n')
            KML_file.write('\t\t\t\t\t</TimeStamp>\n')
            KML_file.write('\t\t\t\t\t<Point> <coordinates>' + l_location[1] + ',' + l_location[0])
            if 'alt' in locals():
                KML_file.write(',' + alt)
                del(alt)
            KML_file.write('</coordinates> </Point>\n')
            KML_file.write('\t\t\t\t</Placemark>\n')

def add_MMF_location(lines, KML_file):
    for line in lines:
        splitted = line.split(' ')
        if 'gps_state_set_aid_mapm:' in splitted:
            l_time = splitted[1]
            for temp in splitted:
                items = temp.split('=')
                if 'iTOW_uint32' in items:
                    iTow =  float(items[1])/1e3
                elif 'flags' in items:
                    if int(items[1]) == 5:
                        flags = 1
                    else:
                        flags = 0
                elif 'latMM' in items:
                    latMM = float(items[1])/1e7
                elif 'lonMM' in items:
                    lonMM = float(items[1])/1e7
                elif 'Heading' in items:
                    heading = float(items[1])/1e2
                    
            KML_file.write('\t\t\t\t<Placemark>\n')
            KML_file.write('\t\t\t\t\t<name>' + l_time + '</name>\n')
            KML_file.write('\t\t\t\t\t<description>\n')
            KML_file.write('\t\t\t\t\t\t<![CDATA[<b>MMF Position</b><br> LogTime: ' + splitted[0] + ' ' + l_time + '<br>')
            KML_file.write(' Latitude: ' + repr(latMM) + '<br> Longitude: ' + repr(lonMM))
            KML_file.write('<br> TOW: ' + repr(iTow))
            KML_file.write('<br> Is tunnel: ' + str(flags))
            KML_file.write('<br> Heading: ' + str(heading))
            KML_file.write(']]>\n')
            KML_file.write('\t\t\t\t\t</description>\n')
            KML_file.write('\t\t\t\t\t<styleUrl>MMF-' + str(flags) + '-Aiding' + str(int(heading)))
            KML_file.write('</styleUrl>\n')
            KML_file.write('\t\t\t\t\t<TimeStamp>\n')
            KML_file.write('\t\t\t\t\t\t<when>' + str(datetime.today().year) + '-' + splitted[0] + 'T' + l_time.split('.')[0] + '</when>\n')
            KML_file.write('\t\t\t\t\t</TimeStamp>\n')
            KML_file.write('\t\t\t\t\t<Point> <coordinates>' + repr(lonMM) + ',' + repr(latMM) + '</coordinates> </Point>\n')
            KML_file.write('\t\t\t\t</Placemark>\n')

def add_track_for_AOSP(lines, KML_file):
    for line in lines:
        splitted = line.split(' ')
        if 'handleMessage(REPORT_LOCATION,' in splitted:
            s_idx = splitted.index('Location[gps')
            l_time = splitted[1]
            l_location = splitted[s_idx+1].split(',')
            if float(l_location[0]) == 0.0 and float(l_location[1]) == 0.0 :
                continue
            for temp in splitted:
                items = temp.split('=')
                if 'alt' in items:
                    alt = items[1]
            KML_file.write(l_location[1] + ',' + l_location[0] )
            if 'alt' in locals():
                KML_file.write(',' + alt + ' ')
                del(alt)
            else:
                KML_file.write(',0 ')
