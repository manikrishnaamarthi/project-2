import sqlite3


def create_user_table():
    conn = sqlite3.connect("fin_user.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fin_users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            email TEXT,
            mobile_number TEXT,
            password TEXT,
            confirm_password TEXT,
            accept_terms TEXT,
            authorize_kyc TEXT,
            customer_status TEXT
        )
    ''')

    conn.commit()


def create_registration_table():
    conn = sqlite3.connect("fin_user.db")
    cursor = conn.cursor()

    # Commit the changes and close the connection
    cursor.execute(''' CREATE TABLE IF NOT EXISTS fin_registration_table (
                                        customer_id INT PRIME NUMBER NOT NULL,
                                        name TEXT,
                                        gender TEXT ,
                                        date_of_birth DATE,
                                        mobile_number INT ,
                                        alternate_mobile_number TEXT,
                                        upload_photo TEXT,
                                        alternate_email TEXT ,
                                        profile_file TEXT,
                                        aadhar_number TEXT,
                                        pan_number TEXT,
                                        aadhar_file TEXT ,
                                        pan_file TEXT, 
                                        highest_qualification TEXT,
                                        tenth_certificate TEXT,
                                        inter_certificate TEXT ,
                                        bachelors_certificate TEXT ,
                                        masters_certificate TEXT,
                                        phd_certificate TEXT,
                                        street_name TEXT ,
                                        relation TEXT,
                                        profession TEXT,
                                        street_address1 TEXT ,
                                        street_address2 TEXT ,
                                        spinner_id1 TEXT ,
                                        spinner_id2 TEXT,
                                        city_name TEXT,
                                        zip_code TEXT,
                                        state_name TEXT,
                                        country_name TEXT,
                                        father_name TEXT, 
                                        father_address TEXT, 
                                        father_occupation TEXT, 
                                        father_ph_no TEXT,
                                        mother_name TEXT, 
                                        mother_address TEXT, 
                                        mother_occupation TEXT, 
                                        mother_ph_no TEXT,
                                        proficient_type TEXT,
                                        college_id TEXT,
                                        collage_name TEXT,
                                        college_address TEXT,
                                        collage_id_file TEXT,
                                        loan_type TEXT,
                                        investment TEXT,
                                        lending_period TEXT,
                                        employment_type TEXT,
                                        company_name TEXT,
                                        organization_type TEXT,
                                        company_address TEXT,
                                        company_pincode TEXT,
                                        company_country TEXT,
                                        landmark TEXT,
                                        business_number TEXT,
                                        annual_salary TEXT,
                                        designation TEXT,
                                        employee_id_file TEXT,
                                        six_months_bank_statement_file TEXT,
                                        account_holder_name TEXT,
                                        spinner_id3 TEXT,
                                        mother_date TEXT,
                                        father_date TEXT,
                                        account_type TEXT,
                                        account_number INT,
                                        bank_name TEXT,
                                        bank_id TEXT,
                                        salary_id TEXT,
                                        branch_name TEXT,
                                        business_name TEXT,
                                        business_location TEXT,
                                        business_address TEXT,
                                        business_branch_name TEXT,
                                        business_type TEXT,
                                        nearest_location TEXT,
                                        no_of_employees_working TEXT,
                                        year_of_estd TEXT,
                                        industry_type TEXT,
                                        last_six_months_turnover TEXT,
                                        last_six_months_turnover_file TEXT,
                                        director_name TEXT,
                                        director_mobile_number TEXT,
                                        DIN TEXT,
                                        CIN TEXT,
                                        registered_office_address TEXT,
                                        proof_of_verification_file TEXT,
                                        marital_status TEXT,
                                        spouse_name TEXT, 
                                        spouse_date_textfield DATE, 
                                        spouse_mobile TEXT, 
                                        spouse_profession TEXT,
                                        spouse_company_name TEXT,
                                        spouse_company_address TEXT, 
                                        spouse_annual_salary TEXT,
                                        spouse_office_no TEXT,
                                        user_type TEXT,
                                        customer_status TEXT
                                        )
                                    ''')

    # Commit the changes and close the connection
    conn.commit()
