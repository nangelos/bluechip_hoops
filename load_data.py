# [sourcecode language="python"]
# Full path and name to your csv file
csv_filepathname="/home/nick/pythonscripts/bluechiphoops/national_recruit_list.csv"

 # Full path to your django project directory
your_djangoproject_home="/home/nick/pythonscripts/bluechiphoops"
import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from basic_app.models import NationalRecruitList
import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar="'")
for row in dataReader:
 if row[0] != 'ZIPCODE': # Ignore the header row, import everything else
    natl = NationalRecruitList()
    natl.player_grad_year = row[0]
    natl.player_rivals_rank = row[1]
    natl.player_espn_rank = row[2]
    natl.player_first_name = row[3]
    natl.player_last_name = row[4]
    natl.player_position = row[5]
    natl.player_school = row[6]
    natl.player_state = row[7]
    natl.player_height = row[8]
    natl.player_weight = row[9]
    natl.player_potential_schools = row[10]
    natl.save()

# [/sourcecode]
