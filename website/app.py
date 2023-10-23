from flask import Flask, render_template
from models.itpracujpl_models import itpracujpl_db_interaction
from models.nofluffjobs_models import nofluffjobs_db_interaction
from models.indeed_models import indeed_db_interaction
app = Flask(__name__)

@app.route('/')
def render_glowna():
    return render_template('right_content/glowna.html', title="Strona Główna")

@app.route('/other_projects')
def display_other_projects():
    return render_template('right_content/other_projects.html', title="Strona Projekty")

@app.route('/danezitpracujpl')
def render_itpracujpl():
    data_dict = {
        "title": "Dane z itpracujpl",
        "count": itpracujpl_db_interaction.positive_salary(),
        "count_etat": itpracujpl_db_interaction.count_etat_data(),
        "count_kontrakt": itpracujpl_db_interaction.count_kontrakt_data(),
        "count_management_level": itpracujpl_db_interaction.count_management_level_data(),
        "count_work_type": itpracujpl_db_interaction.count_work_type_data(),
        "count_spec": itpracujpl_db_interaction.count_specjalizacje_data(),
        "count_technologie_mile_widziane": itpracujpl_db_interaction.count_technologie_mile_widziane_data(),
        "count_technologie_wymagane": itpracujpl_db_interaction.count_technologie_wymagane_data(),
        "count_all": itpracujpl_db_interaction.count_all(),
        "count_locations": itpracujpl_db_interaction.most_common_locations(),
        "salary_counts": itpracujpl_db_interaction.get_salary_counts(),
        "site_link": "https://it.pracuj.pl/praca",
        "site_title": "it.pracuj.pl",
        "chart_data1": itpracujpl_db_interaction.get_historic_count_data(),
        "chart_data2": itpracujpl_db_interaction.get_historic_etat_data(),
        "chart_data3": itpracujpl_db_interaction.get_historic_kontrakt_data(),
        "chart_data4": itpracujpl_db_interaction.get_historic_management_level_data(),
        "chart_data5": itpracujpl_db_interaction.get_historic_work_type_data(),
        "chart_data6": itpracujpl_db_interaction.get_historic_technologie_mile_widziane_data(),
        "chart_data7": itpracujpl_db_interaction.get_historic_technologie_wymagane_data(),
        "chart_data8": itpracujpl_db_interaction.get_historic_location_data(),
    }
    return render_template('right_content/itpracujpl.html', **data_dict)

@app.route('/danezindeed')
def render_indeed():
    data_dict = {
        "title": "Dane z pl.indeed.com",
        "site_link": "https://pl.indeed.com/",
        "site_title": "pl.indeed.com",
        "count_all": indeed_db_interaction.count_all(),
        "count_wynagrodzenie": indeed_db_interaction.wynagrodzenie_data(),
        "count_jezyk": indeed_db_interaction.jezyk_data(),
        "count_tryb": indeed_db_interaction.tryb_data(),
        "count_wymiar": indeed_db_interaction.wymiar_data(),
        "count_wykrztalcenie": indeed_db_interaction.wykrztalcenie_data(),
        "count_lokalizacja": indeed_db_interaction.lokalizacja_data(),
        "count_firmy": indeed_db_interaction.firmy_data(),
        "chart_data1": indeed_db_interaction.get_historic_count_data(),
        "chart_data2": indeed_db_interaction.get_historic_salary_data(),
        "chart_data3": indeed_db_interaction.get_historic_jezyk_data(),
        "chart_data4": indeed_db_interaction.get_historic_tryb_data(),
        "chart_data5": indeed_db_interaction.get_historic_wymiar_data(),
        "chart_data6": indeed_db_interaction.get_historic_wykrztalcenie_data(),
        "chart_data7": indeed_db_interaction.get_historic_firmy_data(),
        "chart_data8": indeed_db_interaction.get_historic_lokalizacja_data(),
    }
    return render_template('right_content/indeed.html', **data_dict)

# TODO w trakcie: zabijania się i historic 

@app.route('/nofluffjobs')
def render_nofluffjobs():
    data_dict = {
        "title": "Dane z nofluffjobs",
        "site_link": "https://nofluffjobs.com/pl",
        "site_title": "nofluffjobs.com",
        "count_all": nofluffjobs_db_interaction.count_all(),
        "salary_counts": nofluffjobs_db_interaction.get_salary_counts(),
        "count_seniority": nofluffjobs_db_interaction.count_seniority_data(),
        "count_category": nofluffjobs_db_interaction.most_common_category(),
        "count_locations": nofluffjobs_db_interaction.count_lokacja_data(),
        "count_doswiadczenie": nofluffjobs_db_interaction.get_doswiadczenie_counts(),
        "count_wymagania_must": nofluffjobs_db_interaction.count_wymagania_must_data(),
        "count_wymagania_nice": nofluffjobs_db_interaction.count_wymagania_nice_data(),
        "chart_data1": nofluffjobs_db_interaction.get_historic_count_data(),
        "chart_data2": nofluffjobs_db_interaction.get_historic_doswiadczenie_data(),
        "chart_data3": nofluffjobs_db_interaction.get_historic_kategoria_data(),
        "chart_data4": nofluffjobs_db_interaction.get_historic_lokacja_data(),
        "chart_data5": nofluffjobs_db_interaction.get_historic_salary_data(),
        "chart_data6": nofluffjobs_db_interaction.get_historic_seniority_data(),
        "chart_data7": nofluffjobs_db_interaction.get_historic_wymagania_must_data(),
        "chart_data8": nofluffjobs_db_interaction.get_historic_wymagania_nice_data(),
    }
    return render_template('right_content/nofluffjobs.html', **data_dict)

@app.route('/about')
def render_about():
    return render_template('right_content/about.html', title="Strona About")

@app.route('/kontakt')
def render_kontakt():
    return render_template('right_content/kontakt.html', title="Strona Kontakt")
