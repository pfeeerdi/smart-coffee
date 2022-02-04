import pandas as pd

def create_coffee_usage_png():
    import pandas as pd
    from app.service.coffee_service import get_hist
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib import dates as mpl_dates

    data = get_hist()
    df = pd.DataFrame()

    dates = [x[:10] for x in data["dates"]]
    time = [x[11:] for x in data["dates"]]

    df["Datum"] = pd.to_datetime(dates)
    df["Uhrzeit"] = time
    df["Art"] = data["coffee_types"]

    #Filter for espresso or double espresso
    filter_db_es = (df["Art"] == "double_espresso")
    d_espresso_df = df.loc[filter_db_es]
    filter_es = (df["Art"] == "espresso")
    espresso_df = df.loc[filter_es]

    #sort by time
    d_espresso_df = d_espresso_df.sort_values(by=['Uhrzeit'])
    espresso_df = espresso_df.sort_values(by=['Uhrzeit'])

    #variables for plotting
    es_datum = espresso_df["Datum"]
    es_art = espresso_df["Art"]
    es_zeit = espresso_df["Uhrzeit"]
    db_es_datum = d_espresso_df["Datum"]
    db_es_art = espresso_df["Art"]
    db_es_zeit = d_espresso_df["Uhrzeit"]

    # #All Plot
    # plt.plot_date(es_datum, es_zeit, "ro")
    # plt.plot_date(db_es_datum, db_es_zeit, "bo")
    # plt.gcf().autofmt_xdate()
    # date_format = mpl_dates.DateFormatter("%b, %d %Y")
    # plt.gca().xaxis.set_major_formatter(date_format)
    # plt.title("Konsum von Espressi und Doppelten Espressi")
    # plt.xlabel("Datum")
    # plt.ylabel("Uhrzeit")
    # plt.tight_layout()
    # plt.savefig("pics/all_usage.png")
    # plt.close()
    # Espresso Plt
    plt.plot_date(es_datum, es_zeit, "ro")
    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter("%d %b %Y")
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.title("Konsum von Espressi")
    plt.xlabel("Datum")
    plt.ylabel("Uhrzeit")
    plt.tight_layout()
    plt.savefig("pics/espresso_usage.png")
    plt.close()
    #Double Espresso Plot
    plt.plot_date(db_es_datum, db_es_zeit, "ro")
    plt.gcf().autofmt_xdate()
    plt.gca().xaxis.set_major_formatter(date_format)
    plt.title("Konsum von doppelten Espressi")
    plt.xlabel("Datum")
    plt.ylabel("Uhrzeit")
    plt.tight_layout()
    plt.savefig("pics/double_espresso_usage.png")
    plt.close()

