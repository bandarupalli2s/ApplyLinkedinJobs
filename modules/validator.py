# from config.XdepricatedX import *

from typing import Union, List

__validation_file_path = ""

def check_int(var: int, var_name: str, min_value: int=0) -> Union[bool, TypeError, ValueError]:
    '''
    Validates if the given variable is an integer and greater than or equal to min_value.
    '''
    if not isinstance(var, int):
        raise TypeError(f"{var_name} must be an integer, got {type(var).__name__}")
    if var < min_value:
        raise ValueError(f"{var_name} must be greater than or equal to {min_value}, got {var}")
    return True

def check_boolean(var: bool, var_name: str) -> Union[bool, ValueError]:
    '''
    Validates if the given variable is a boolean.
    '''
    if not isinstance(var, bool):
        raise ValueError(f"{var_name} must be a boolean (True or False), got {type(var).__name__}")
    return True

def check_string(var: str, var_name: str, options: List=[], min_length: int=0) -> Union[bool, TypeError, ValueError]:
    '''
    Validates if the given variable is a string and meets the specified criteria.
    '''
    if not isinstance(var, str):
        raise TypeError(f"{var_name} must be a string, got {type(var).__name__}")
    if len(var) < min_length:
        raise ValueError(f"{var_name} must be at least {min_length} characters long, got {len(var)}")
    if options and var not in options:
        raise ValueError(f"{var_name} must be one of {options}, got '{var}'")
    return True

def check_list(var: list, var_name: str, options: List=[], min_length: int=0) -> Union[bool, TypeError, ValueError]:
    '''
    Validates if the given variable is a list and meets the specified criteria.
    '''
    if not isinstance(var, list):
        raise TypeError(f"{var_name} must be a list, got {type(var).__name__}")
    if len(var) < min_length:
        raise ValueError(f"{var_name} must have at least {min_length} items, got {len(var)}")
    if options:
        for item in var:
            if item not in options:
                raise ValueError(f"{var_name} contains invalid item '{item}', must be one of {options}")
    return True

from config.personals import *
def validate_personals() -> Union[None, ValueError, TypeError]:
    '''
    Validates all variables in the `/config/personals.py` file.
    '''
    global __validation_file_path
    __validation_file_path = "config/personals.py"

    check_string(first_name, "first_name", min_length=1)
    check_string(middle_name, "middle_name")
    check_string(last_name, "last_name", min_length=1)

    check_string(phone_number, "phone_number", min_length=10)

    check_string(current_city, "current_city")
    
    check_string(street, "street")
    check_string(state, "state")
    check_string(zipcode, "zipcode")
    check_string(country, "country")
    
    check_string(ethnicity, "ethnicity", ["Decline", "Hispanic/Latino", "American Indian or Alaska Native", "Asian", "Black or African American", "Native Hawaiian or Other Pacific Islander", "White", "Other"],  min_length=0)
    check_string(gender, "gender", ["Male", "Female", "Other", "Decline", ""])
    check_string(disability_status, "disability_status", ["Yes", "No", "Decline"])
    check_string(veteran_status, "veteran_status", ["Yes", "No", "Decline"])

from config.questions import *
def validate_questions() -> Union[None, ValueError, TypeError]:
    '''
    Validates all variables in the `/config/questions.py` file.
    '''
    global __validation_file_path
    __validation_file_path = "config/questions.py"

    check_string(default_resume_path, "default_resume_path")
    check_string(years_of_experience, "years_of_experience")
    check_string(require_visa, "require_visa", ["Yes", "No"])
    check_string(website, "website")
    check_string(linkedIn, "linkedIn")
    check_int(desired_salary, "desired_salary")
    check_string(us_citizenship, "us_citizenship", ["U.S. Citizen/Permanent Resident", "Non-citizen allowed to work for any employer", "Non-citizen allowed to work for current employer", "Non-citizen seeking work authorization", "Canadian Citizen/Permanent Resident", "Other"])
    check_string(linkedin_headline, "linkedin_headline")
    check_int(notice_period, "notice_period")
    check_int(current_ctc, "current_ctc")
    check_string(linkedin_summary, "linkedin_summary")
    check_string(cover_letter, "cover_letter")
    check_string(recent_employer, "recent_employer")
    check_string(confidence_level, "confidence_level")

    check_boolean(pause_before_submit, "pause_before_submit")
    check_boolean(pause_at_failed_question, "pause_at_failed_question")
    check_boolean(overwrite_previous_answers, "overwrite_previous_answers")

from config.search import *
def validate_search() -> Union[None, ValueError, TypeError]:
    '''
    Validates all variables in the `/config/search.py` file.
    '''
    global __validation_file_path
    __validation_file_path = "config/search.py"

    check_list(search_terms, "search_terms", min_length=1)
    check_string(search_location, "search_location")
    check_int(switch_number, "switch_number", 1)
    check_boolean(randomize_search_order, "randomize_search_order")

    check_string(sort_by, "sort_by", ["", "Most recent", "Most relevant"])
    check_string(date_posted, "date_posted", ["", "Any time", "Past month", "Past week", "Past 24 hours"])
    check_string(salary, "salary")

    check_boolean(easy_apply_only, "easy_apply_only")

    check_list(experience_level, "experience_level", ["Internship", "Entry level", "Associate", "Mid-Senior level", "Director", "Executive"])
    check_list(job_type, "job_type", ["Full-time", "Part-time", "Contract", "Temporary", "Volunteer", "Internship", "Other"])
    check_list(on_site, "on_site", ["On-site", "Remote", "Hybrid"])

    check_list(companies, "companies")
    check_list(location, "location")
    check_list(industry, "industry")
    check_list(job_function, "job_function")
    check_list(job_titles, "job_titles")
    check_list(benefits, "benefits")
    check_list(commitments, "commitments")

    check_boolean(under_10_applicants, "under_10_applicants")
    check_boolean(in_your_network, "in_your_network")
    check_boolean(fair_chance_employer, "fair_chance_employer")

    check_boolean(pause_after_filters, "pause_after_filters")

    check_list(about_company_bad_words, "about_company_bad_words")
    check_list(about_company_good_words, "about_company_good_words")
    check_list(bad_words, "bad_words")
    check_boolean(security_clearance, "security_clearance")
    check_boolean(did_masters, "did_masters")
    check_int(current_experience, "current_experience", -1)

from config.secrets import *
def validate_secrets() -> Union[None, ValueError, TypeError]:
    '''
    Validates all variables in the `/config/secrets.py` file.
    '''
    global __validation_file_path
    __validation_file_path = "config/secrets.py"

    check_string(username, "username", min_length=5)
    check_string(password, "password", min_length=5)

    check_boolean(use_AI, "use_AI")
    check_string(llm_api_url, "llm_api_url", min_length=5)
    check_string(llm_api_key, "llm_api_key")
    check_string(llm_model, "llm_model")
    # check_string(llm_embedding_model, "llm_embedding_model")
    check_boolean(stream_output, "stream_output")
    
    ##> ------ Yang Li : MARKYangL - Feature ------
    # Validate DeepSeek configuration
    check_string(ai_provider, "ai_provider", ["openai", "deepseek"])
    check_string(deepseek_api_url, "deepseek_api_url", min_length=5)
    check_string(deepseek_api_key, "deepseek_api_key")
    check_string(deepseek_model, "deepseek_model", ["deepseek-chat", "deepseek-reasoner"])
    ##<

from config.settings import *
def validate_settings() -> Union[None, ValueError, TypeError]:
    '''
    Validates all variables in the `/config/settings.py` file.
    '''
    global __validation_file_path
    __validation_file_path = "config/settings.py"

    check_boolean(close_tabs, "close_tabs")
    check_boolean(follow_companies, "follow_companies")
    # check_boolean(connect_hr, "connect_hr")
    # check_string(connect_request_message, "connect_request_message", min_length=10)

    check_boolean(run_non_stop, "run_non_stop")
    check_boolean(alternate_sortby, "alternate_sortby")
    check_boolean(cycle_date_posted, "cycle_date_posted")
    check_boolean(stop_date_cycle_at_24hr, "stop_date_cycle_at_24hr")
    
    # check_string(generated_resume_path, "generated_resume_path", min_length=1)

    check_string(file_name, "file_name", min_length=1)
    check_string(failed_file_name, "failed_file_name", min_length=1)
    check_string(logs_folder_path, "logs_folder_path", min_length=1)

    check_int(click_gap, "click_gap", 0)

    check_boolean(run_in_background, "run_in_background")
    check_boolean(disable_extensions, "disable_extensions")
    check_boolean(safe_mode, "safe_mode")
    check_boolean(smooth_scroll, "smooth_scroll")
    check_boolean(keep_screen_awake, "keep_screen_awake")
    check_boolean(stealth_mode, "stealth_mode")

def validate_config() -> Union[bool, ValueError, TypeError]:
    '''
    Runs all validation functions to validate all variables in the config files.
    '''
    validate_personals()
    validate_questions()
    validate_search()
    validate_secrets()
    validate_settings()

    # validate_String(chatGPT_username, "chatGPT_username")
    # validate_String(chatGPT_password, "chatGPT_password")
    # validate_String(chatGPT_resume_chat_title, "chatGPT_resume_chat_title")
    return True

