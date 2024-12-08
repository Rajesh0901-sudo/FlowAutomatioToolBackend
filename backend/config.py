import json,os

envs_file = "data/envs.json"


def env_file_exist():
    try:
        if not os.path.exists(envs_file):
            print("Configuration env file not found")
            return False
        
        else:
            return True
    
    except Exception as e:
        print("an error occured while opening env files",e)
        return False


def load_env_config(env_name):

    if env_file_exist() != True:
        return None

    try:

        with open (envs_file,"r") as file:
            envs = json.load(file)

        if env_name not in envs:
            print("env not found")
            return None
        
        return envs[env_name]
    
    except Exception as e:
        print("an error occured while opening env files",e)

def add_env_config(env_name,configurations):

    if env_file_exist() != True:
        return 0
    
    try:

        with open (envs_file,"r") as file:
            envs = json.load(file)

        if env_name in envs:
            print("env already exist")
            return 0
        
        envs[env_name] = configurations

        with open (envs_file,"w") as file:
            json.dump(envs, file, indent=4)
        
        print("Env added successfully")

        return 1
    
    except Exception as e:
        print("an error occured while opening env files",e)


def update_env_config(env_name,newConfigurations):

    if env_file_exist() != True:
        return 0
    
    try:

        with open (envs_file,"r") as file:
            envs = json.load(file)

        if env_name not in envs:
            print("env does not exist")
            return 0
        
        envs[env_name] = newConfigurations

        with open (envs_file,"w") as file:
            json.dump(envs, file, indent=4)
        
        print("Env added successfully")

        return 1
    
    except Exception as e:
        print("an error occured while opening env files",e)