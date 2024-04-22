import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

from daily_planner_app import DailyPlannerApp

def main():
    window = DailyPlannerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()