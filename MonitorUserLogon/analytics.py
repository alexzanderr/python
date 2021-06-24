

from MonitorUserLogon.imports import *



results_folder = Path("results")
if not results_folder.exists():
    raise FileNotFoundError(results_folder.as_posix())


analytics_folder = Path("analytics")
if not analytics_folder.exists():
    analytics_folder.mkdir()


remote_analytics_folder = Path(r"D:\Alexzander__\PythonApplicationsAppData\MonitorUserLogon\analytics")
if not remote_analytics_folder.exists():
    remote_analytics_folder.mkdir()


def PlotCurrentDate():
    current_date = datetime__.get_current_date()

    for file in results_folder.iterdir():
        if current_date in file.name:
            # found the current date metadata
            metadata = json.loads(file.read_text())
            user_online = [metadata["online"]]
            user_offline = [metadata["offline"]]


            total = datetime__.seconds_to_time(metadata["total"])

            labels = [f"Total: {total.hours} hours {total.minutes} minutes {total.seconds} seconds"]
            width = 0.15

            fig, ax = plt.subplots(figsize=(13, 8))

            online = datetime__.seconds_to_time(metadata["online"])
            activity = f"Activity: {online.hours} hours {online.minutes} minutes {online.seconds} seconds"
            ax.bar(labels, user_online, width, yerr=[2], label=activity)

            offline = datetime__.seconds_to_time(metadata["offline"])
            inactivity = f"Inactivity: {offline.hours} hours {offline.minutes} minutes {offline.seconds} seconds"

            ax.bar(labels, user_offline, width, yerr=[3], bottom=user_online,
                label=inactivity)

            ax.set_ylabel('Seconds')
            ax.set_title(f'User Logon Activity: [  {current_date}  ]')
            ax.legend()

            file_name = (current_date + "_plot.png")
            figure = analytics_folder / file_name
            plt.savefig(figure.as_posix())

            remote_figure = remote_analytics_folder / file_name
            plt.savefig(remote_figure.as_posix())



def SubprocessPlot():
    subprocess.call(["python.exe", "analytics.py"])

if __name__ == '__main__':
    PlotCurrentDate()