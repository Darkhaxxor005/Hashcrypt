a
    ���a�U �                   @   s�  d Z ddlZddlmZ ddlZddlmZ ddlZddl	Z
ddlZddlZdd� Zdd� Ze�� ejd	d
ded�ejddejddd�dd�ejdddedd�ejddddd�ejddddd�ejd d!ded"d�ejd#dd$d�ejd%dd&d�ejd'dd(d�ejd)d*ded+d,�d-d.� �����������Zd/d0� Zd1d2ifeed3�d4d5�Zd1d2ifeed3�d6d7�Zi feed3�d8d9�Zed:k�r�e�  dS );aT  

MIIEpQIBAAKCAQEAmDmgQAXKaHyTUVf3h/skxS3zVrsdT/8vK9hIl+swQ66sUAqw
ZJDhSX7HposlKgdz6TtVzWLZr/s1m1lJCzCGFbxTHA+w7dsG0qkuhAdZzx1mTHXk
Uhs0sNMq/PsWTGzBJAJvKtqY+/c1IOKKadt5EBxm9RPnK6BAktD+vr9XnNODGjr1
8yqEOmFELHrwpNNKa8NLqxYiCiQV58DE/5NO0V/OqNLlkwR8KNM9BooeTYRG+A3J
2ZfKIrvhFLVXiVRRn/p2ZwB23hFJMT91UOVbvJa5Gpm2RrIe9rUxuF6srD8fnkOU
CJh4FbPJleHZyC7KYOOhAcjPNCu5NI4a5H2oCQIDAQABAoIBAC9FHcUjxzHhFWIa
HeylCUsNtNXG7xhLVtuXoxtB1k/+KtYEK7he4QaQjvDhnp3JiK3xVficbJrgOEpQ
VIVcARc4ztoU6U1DSYAbNy2alsHhEEZICamRdzA9ssiyM79xuhwzgU/eZ8k+f8oB
bxfmJlbhavtJvexnLAYrTh/vjQZOkXomAYSQJya72CfpDxWkiPEOJjBSSib2j9yY
0x5F/M8eVhB48LNvoPvbkW/FsnlJAerKIOYQZQA8NgZkBpCbanVnJ0XT10M68+lT
Wa+8+fZcsSnby6Arkr0MkJdeSJdeAYrWpLoqJyEozhUJvxgtjdIJM81bf2Sl+zJr
WcMIjPECgYEAxh81bnaQ+19V1S0gWaHxQzbnqtwNZ47YrZnB9bkkvrBtYvRR1ev9
170Dt7c0AomyY50mP4efp3ZgJJ2OYWSg0exB6kgblIj89rFQWGJwMQrWoSSqK1Fk
WswFKzfI7qrdnB8Xzvly3lI+alJd2HYSO9xvo8A05ly8/lxVEE/aO20CgYEAxLH3
yMp7X4jGykNN31IJR9TGznPt5BcuFmL+eT6X/EIquRuHLCb6TzDR1OT6LSMWxPqS
dVKx97hH4gT7gDSAPNVGS1NFx+PQMPwzdLIYG/9eW+GyPPRu7SEmEs489V75uTmB
PRFGNwM5M94Khpx8AgmkSHKiDT523t3Thk4dgY0CgYEAvkJKNYJ3SG8NJmLnpiv2
XO3lHBemZ8SuIEiAE1FxEA6tfVHTJPQ0GXHSmCK/N5C0VyUbDfdYQqFTQtZrXOwd
5HpV8n68va+v/dfZqIcf5njaFHX5VRAcp3U1oYM42roLh1n0qzayMP4aIlBm/vCk
IghWzZJPOsnkVQCmT7vffyECgYEAhu9L+9wkPMqZDSKU5nHh2fw3EmRnO0VHoaXx
yv1MyIofwvMGjRyENRVZrYITuilLMoBvPrsnSbiK35vpaO8bViA9Y+lRgqpfJWuu
ZQzUC0jp04CGhNhuzJAkDVycZvvrtsyjQ2B5Wb4FXPajI+twCvnQUL8LOqiyZXup
44XtKfUCgYEAs8DsRxHqL/nu9akH5MWKqxKsH1oeUeMTL0MLkBpJKkLnAu/pSQz9
y41V0jYgz7hO9Voiv1xaFRlXbhP75RzaEwDf5afDDJbsU1jsXMmcXvcAEGUG3s6p
NcPjjBvjld4EM+nuFCY6C62819jmD/jQ2FzA5hMiPne4tGb+JLO5cAg=

�    N)�List��printc                 C   s   t �| �� � | ��  d S �N)�click�echo�get_help�exit)�ctx� r   �tool.py�
print_helpV  s    r   c                  C   s   d} t | � d S )Na\  [bold green]

                                                                       
                                                                         
                                       .#@@@@#*            @@&&                 
                                @&@@@@@@*    ,@@&@@@@@@@@@@,                    
                             @@@@                      (                        
                           @@@        &@@@@@@@@@@@                              
                         .@@*      @@@%          @@@@                           
                        %@@,     @@@               %@@                          
   /@@@@@@&&&&&&&&@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@@&&&&&&&&&&&&@@@@@&&@&@@% 
                      @@@@@      @&          &@%    #@@                         
                     @@# @@@      @@@      #@@@     @@/                         
                    @@    .@@@       @@@@@@@      *@@.                          
                  /@@       ,@@@                @@@.                            
                 @&&&@@@@@@@@@@@@@@@@@@&&@@@@@&@           

    r   )�textr   r   r   �banner[  s    r   z-tz--textzLCheck one hash, use single quotes ' as inverted commas " messes up on Linux.)�help�typez-fz--file�rzutf-8)�encodingz.Checks every hash in a newline separated file.)r   r   z-gz--greppableTz9Are you going to grep this output? Prints in JSON format.)�is_flagr   r   z-b64z--base64z�Decodes hashes in Base64 before identification. For files with mixed Base64 & non-encoded it attempts base64 first and then falls back to normal hash identification per hash.)r   r   z-az--accessiblez�Turn on accessible mode, does not print ASCII art. Also does not print very large blocks of text, as this can cause some pain with screenreaders. This reduces the information you get. If you want the least likely feature but no banner, use --no-banner. z-ez	--extremez�Searches for hashes within a string. This mode will get 5d41402abc4b2a76b9719d911017c592 from ####5d41402abc4b2a76b9719d911017c592###z--no-bannerzRemoves banner from startup.z	--no-johnz(Don't print John The Ripper Information.z--no-hashcatz Don't print Hashcat Information.z-vz	--verbosez.Turn on debugging logs. -vvv for maximum logs.)�countr   r   c                  K   sF  d}| � � D ]}|rd} qq|rdt�t��(}t�t�|�� td� W d  � n1 sZ0    Y  t| � t�	| � | d s�| d s�| d s�t�
d� t�  t�tj�}t�| �}t�| |�}t�	d	� g }| d
 r�|�| d
 � |j}n2| d �r|�| d � |j}n| d �r|�� }| d �r8t|�|�� n
|�|� dS )z}
Author:R00tdev1l
Email:indradas4863@gmail.com
Join Our Facebook Group: https://www.facebook.com/groups/1174653339565169
    TFr   NZ
accessibleZ	no_bannerZ	greppablezRunning the banner.z;Initialised the hash_info, nth, and pretty_printer objects.r   �fileZextreme)�valuesr   ZContext�mainr   r   r	   �set_logging�logging�debug�infor   �
hash_namer�Name_That_Hash�hashes�
prototypes�
prettifier�
Prettifier�check_hashes�HashChecker�single_hash�outputZ
file_inputZfind_all_hashesr   �greppable_outputZpretty_print)�kwargsZno_args�ir
   �nth�pretty_printer�hashCheckerr&   r   r   r   r   q  s<    9&






r   c                 C   s.   | d rt jt jddd� nt jt jd� d S )N�verbosez%(asctime)s - %(message)sz%d-%b-%y %H:%M:%S)�level�formatZdatefmt)r.   )r   ZbasicConfig�DEBUGZCRITICAL)r(   r   r   r   r   �  s    �r   Zpopular_onlyF)�chash�argsc                 C   s   t j|dd�}|�t| |��S )z�
    Using name-that-hash as an API? Call this function!

    Given a list of hashes of strings
    return a list of json of all hashes in the same order as the input
    T�Zapi)r!   r"   r'   �compute_hashes_for_api�r1   r2   r+   r   r   r   �api_return_hashes_as_json�  s    r6   c                 C   s   t j|dd�}|�t| |��S )z/
    Returns hashes as a Python dictionary
    Tr3   )r!   r"   Zturn_hash_objs_into_dictr4   r5   r   r   r   �api_return_hashes_as_dict�  s    r7   c                 C   s2   t �tj�}t�||�}| D ]}|�|� q|jS r   )r   r   r   r    r#   r$   r%   r&   )r1   r2   r*   r,   r)   r   r   r   r4   �  s
    r4   �__main__)�__doc__r   �typingr   r   Zrichr   Zmodule3r#   Zmodule4r   Zmodule5r   Zmodule6r!   r   r   Zcommand�option�strZFile�bool�intr   r   �dictr6   r7   r4   �__name__r   r   r   r   �<module>   s�         J��������3
     D