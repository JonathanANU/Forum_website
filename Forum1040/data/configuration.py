# This configuration file gets the path of the database file
# so that we can access the 1040.db file from other directories
# as well
import os.path

package_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(package_dir, '1040.db')
