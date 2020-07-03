# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['SchemaTestCase::test_form_to_schema 1'] = {
    'properties': {
        'Age': {
            'description': 'Age of the participant',
            'name': 'Age',
            'type': 'string'
        },
        'Carrying': {
            'choices': [
                'Yes',
                'No'
            ],
            'description': '"Are you carrying Naloxone Today?"',
            'name': 'Carrying',
            'type': 'string'
        },
        'Category_Friend': {
            'name': 'Category_Friend',
            'type': 'boolean'
        },
        'Category_Other': {
            'name': 'Category_Other',
            'type': 'boolean'
        },
        'Category_Other_text': {
            'description': '"Which category best descirbes you?" "Other" checked, additional information (free text)',
            'name': 'Category_Other_text',
            'type': 'string'
        },
        'Category_Parent': {
            'name': 'Category_Parent',
            'type': 'boolean'
        },
        'Category_Provider': {
            'name': 'Category_Provider',
            'type': 'boolean'
        },
        'Category_Recover': {
            'name': 'Category_Recover',
            'type': 'boolean'
        },
        'Category_Uses': {
            'name': 'Category_Uses',
            'type': 'boolean'
        },
        'DOB_Day': {
            'description': 'Day of the month the pariticpant was born.',
            'name': 'DOB_Day',
            'type': 'string'
        },
        'DOB_Month': {
            'description': 'Month the participant was born.',
            'name': 'DOB_Month',
            'type': 'string'
        },
        'DOB_Year': {
            'description': 'Year the participant was born.',
            'name': 'DOB_Year',
            'type': 'string'
        },
        'Date': {
            'description': 'Date the form was signed',
            'name': 'Date',
            'type': 'string'
        },
        'Date_Day': {
            'description': 'Day of the month the training was performed.',
            'name': 'Date_Day',
            'type': 'string'
        },
        'Date_Month': {
            'description': 'Month the training was performed.',
            'name': 'Date_Month',
            'type': 'string'
        },
        'Date_Year': {
            'description': 'Year the training was performed.',
            'name': 'Date_Year',
            'type': 'string'
        },
        'Gender': {
            'description': 'Gender of the participant (free text)',
            'name': 'Gender',
            'type': 'string'
        },
        'Health_Arrhy': {
            'name': 'Health_Arrhy',
            'type': 'boolean'
        },
        'Health_Asthma': {
            'name': 'Health_Asthma',
            'type': 'boolean'
        },
        'Health_Bipolar': {
            'name': 'Health_Bipolar',
            'type': 'boolean'
        },
        'Health_COPD': {
            'name': 'Health_COPD',
            'type': 'boolean'
        },
        'Health_Diabetes': {
            'name': 'Health_Diabetes',
            'type': 'boolean'
        },
        'Health_Emph': {
            'name': 'Health_Emph',
            'type': 'boolean'
        },
        'Health_Endo': {
            'name': 'Health_Endo',
            'type': 'boolean'
        },
        'Health_HBP': {
            'name': 'Health_HBP',
            'type': 'boolean'
        },
        'Health_HD': {
            'name': 'Health_HD',
            'type': 'boolean'
        },
        'Health_ID': {
            'name': 'Health_ID',
            'type': 'boolean'
        },
        'Health_Kidney': {
            'name': 'Health_Kidney',
            'type': 'boolean'
        },
        'Health_Liver': {
            'name': 'Health_Liver',
            'type': 'boolean'
        },
        'Health_Other': {
            'name': 'Health_Other',
            'type': 'boolean'
        },
        'Health_Other_text': {
            'description': '"Have you ever been diagnosed with any of the following health conditions? (Check all that apply.)" "Other" checked, additional information (free text)',
            'name': 'Health_Other_text',
            'type': 'string'
        },
        'Health_Schizo': {
            'name': 'Health_Schizo',
            'type': 'boolean'
        },
        'Health_Seizures': {
            'name': 'Health_Seizures',
            'type': 'boolean'
        },
        'Insurance': {
            'choices': [
                'Yes',
                'No'
            ],
            'description': '"Do you currently have insurance?" ',
            'name': 'Insurance',
            'type': 'string'
        },
        'IsStaff': {
            'description': '"Check if you are a staff member"',
            'name': 'IsStaff',
            'type': 'boolean'
        },
        'Name': {
            'description': 'Name of participant (free text)',
            'name': 'Name',
            'type': 'string'
        },
        'OD_outcome_EMS': {
            'name': 'OD_outcome_EMS',
            'type': 'boolean'
        },
        'OD_outcome_ER': {
            'name': 'OD_outcome_ER',
            'type': 'boolean'
        },
        'OD_outcome_Police': {
            'name': 'OD_outcome_Police',
            'type': 'boolean'
        },
        'OD_outcome_Unknown': {
            'name': 'OD_outcome_Unknown',
            'type': 'boolean'
        },
        'OD_recent': {
            'description': 'if yes to Overdose: "When was your most recent overdose?" (free text)',
            'name': 'OD_recent',
            'type': 'string'
        },
        'OD_times': {
            'description': 'If yes to Overdose: "How many times?" (free text)',
            'name': 'OD_times',
            'type': 'string'
        },
        'Opiates': {
            'choices': [
                'Yes',
                'No'
            ],
            'description': '"In the last 90 days, have you gone 3 or more days without opiates?',
            'name': 'Opiates',
            'type': 'string'
        },
        'Opiates_Break': {
            'description': 'If yes to opiates: "If YES, why?" "Decided to take a break" checked',
            'name': 'Opiates_Break',
            'type': 'string'
        },
        'Opiates_Hospital': {
            'description': 'If yes to opiates: "If YES, why?" "Hospital" checked',
            'name': 'Opiates_Hospital',
            'type': 'string'
        },
        'Opiates_Jail': {
            'description': 'If yes to opiates: "If YES, why?" "Jail checked',
            'name': 'Opiates_Jail',
            'type': 'string'
        },
        'Opiates_Money': {
            'description': 'If yes to opiates: "If YES, why?" "No money" checked',
            'name': 'Opiates_Money',
            'type': 'string'
        },
        'Opiates_Other': {
            'description': 'If yes to opiates: "If YES, why?" "Other" checked',
            'name': 'Opiates_Other',
            'type': 'string'
        },
        'Opiates_Other_text': {
            'description': 'If yes to opiates: "If YES, why?" "Other" checked, additional information (free text)',
            'name': 'Opiates_Other_text',
            'type': 'boolean'
        },
        'Opiates_Treatment': {
            'description': 'If yes to opiates: "If YES, why?" "Inpatient/Outpatient Drug Treatment" checked',
            'name': 'Opiates_Treatment',
            'type': 'string'
        },
        'Overdose': {
            'choices': [
                'Yes',
                'No'
            ],
            'description': '"Have you ever overdosed before?"',
            'name': 'Overdose',
            'type': 'string'
        },
        'Race': {
            'description': 'Race of the participant (free text)',
            'name': 'Race',
            'type': 'string'
        },
        'SEP': {
            'description': "Last 4 digits of the participant's social security",
            'name': 'SEP',
            'type': 'string'
        },
        'Staff': {
            'description': 'Staff member who signed the form',
            'name': 'Staff',
            'type': 'string'
        },
        'UniqueID': {
            'description': 'Unique ID of the participant',
            'name': 'UniqueID',
            'type': 'string'
        },
        'Useage_Ativan': {
            'name': 'Useage_Ativan',
            'type': 'boolean'
        },
        'Useage_Cocaine': {
            'name': 'Useage_Cocaine',
            'type': 'boolean'
        },
        'Useage_Codeine': {
            'name': 'Useage_Codeine',
            'type': 'boolean'
        },
        'Useage_Fentanyl': {
            'name': 'Useage_Fentanyl',
            'type': 'boolean'
        },
        'Useage_Heroin': {
            'name': 'Useage_Heroin',
            'type': 'boolean'
        },
        'Useage_K2': {
            'name': 'Useage_K2',
            'type': 'boolean'
        },
        'Useage_Methadone': {
            'name': 'Useage_Methadone',
            'type': 'boolean'
        },
        'Useage_Other': {
            'name': 'Useage_Other',
            'type': 'boolean'
        },
        'Useage_OtherOpiates': {
            'name': 'Useage_OtherOpiates',
            'type': 'boolean'
        },
        'Useage_Other_text': {
            'description': '"In the last 90 days, have you used:"  "Other" checked, additional information (free text)',
            'name': 'Useage_Other_text',
            'type': 'string'
        },
        'Useage_Oxy': {
            'name': 'Useage_Oxy',
            'type': 'boolean'
        },
        'Useage_Valium': {
            'name': 'Useage_Valium',
            'type': 'boolean'
        },
        'Useage_Vicodin': {
            'name': 'Useage_Vicodin',
            'type': 'boolean'
        },
        'Useage_Xanax': {
            'name': 'Useage_Xanax',
            'type': 'boolean'
        },
        'Who_Carry': {
            'name': 'Who_Carry',
            'type': 'boolean'
        },
        'Who_Client': {
            'name': 'Who_Client',
            'type': 'boolean'
        },
        'Who_Family': {
            'name': 'Who_Family',
            'type': 'boolean'
        },
        'Who_Friend': {
            'name': 'Who_Friend',
            'type': 'boolean'
        },
        'Who_Yourself': {
            'name': 'Who_Yourself',
            'type': 'boolean'
        },
        'Witness': {
            'choices': [
                'Yes',
                'No'
            ],
            'description': '"Have you ever witnessed a drug overdose?"',
            'name': 'Witness',
            'type': 'string'
        },
        'Witness_largenum': {
            'description': 'If 21+ checked, how many? (free text)',
            'name': 'Witness_largenum',
            'type': 'string'
        },
        'Witness_recent': {
            'choices': [
                '< 1 week',
                '1 week to 1 month',
                '1-3 months',
                '> 3 months'
            ],
            'description': '"When was the last time you witnessed an overdose?"',
            'name': 'Witness_recent',
            'type': 'string'
        },
        'Witness_times': {
            'choices': [
                '<5',
                '5-10',
                '11-15',
                '16-20',
                '21+'
            ],
            'description': '"If YES, how many?"',
            'name': 'Witness_times',
            'type': 'string'
        }
    },
    'type': 'object'
}

snapshots['SchemaTestCase::test_form_to_schema 2'] = {
    'properties': {
        'Breathing': {
            'description': 'Participant Initialed in the "Rescue Breathing" box',
            'name': 'Breathing',
            'type': 'boolean'
        },
        'Call911': {
            'description': 'Participant Initialed in the "911 Calls & Working with EMTS" box',
            'name': 'Call911',
            'type': 'boolean'
        },
        'DOB_Day': {
            'description': 'Day of the month the pariticpant was born.',
            'name': 'DOB_Day',
            'type': 'string'
        },
        'DOB_Month': {
            'description': 'Month the participant was born.',
            'name': 'DOB_Month',
            'type': 'string'
        },
        'DOB_Year': {
            'description': 'Year the participant was born.',
            'name': 'DOB_Year',
            'type': 'string'
        },
        'Date_Day': {
            'description': 'Day of the month the form was signed',
            'name': 'Date_Day',
            'type': 'string'
        },
        'Date_Month': {
            'description': 'Month the form was signed',
            'name': 'Date_Month',
            'type': 'string'
        },
        'Date_Year': {
            'description': 'Year the form was signed',
            'name': 'Date_Year',
            'type': 'string'
        },
        'ExpDate': {
            'description': '(free text)',
            'name': 'ExpDate',
            'type': 'string'
        },
        'LotNum': {
            'description': '(free text)',
            'name': 'LotNum',
            'type': 'string'
        },
        'Medication': {
            'choices': [
                'SHP',
                'SEP',
                'CM',
                'WN',
                'WCC',
                'Drop In',
                'Testing',
                'External (provider/parent/community)'
            ],
            'description': '"What program\'s medication was used for training if applicable?"',
            'name': 'Medication',
            'type': 'string'
        },
        'Naloxone': {
            'description': 'Participant Initialed in the "Naloxone" box',
            'name': 'Naloxone',
            'type': 'boolean'
        },
        'Name': {
            'description': "Participant's name (free text)",
            'name': 'Name',
            'type': 'string'
        },
        'Risk': {
            'description': 'Participant Initialed in the "Overdose Risk Factors" box',
            'name': 'Risk',
            'type': 'boolean'
        },
        'Safety': {
            'description': 'Participant Initialed in the "Rescue Safety" box',
            'name': 'Safety',
            'type': 'boolean'
        },
        'Signature': {
            'description': 'The participant signed the form giving Prevention Point Philadelphia permission to verify that the participant has completed Opiate Overdose Prevention Training',
            'name': 'Signature',
            'type': 'boolean'
        },
        'Staff': {
            'description': 'Staff memember who lead the training (free text)',
            'name': 'Staff',
            'type': 'string'
        },
        'Symptoms': {
            'description': 'Participant Initialed in the "Overdose Symptoms Recognition" box',
            'name': 'Symptoms',
            'type': 'boolean'
        },
        'Trained': {
            'choices': [
                'SHP',
                'SEP',
                'CM',
                'WN',
                'WCC',
                'Drop In',
                'Testing',
                'External (provider/parent/community)'
            ],
            'description': '"What program did the person who trained you come from?"',
            'name': 'Trained',
            'type': 'string'
        },
        'UniqueID': {
            'description': 'Unique ID of the participant ',
            'name': 'UniqueID',
            'type': 'string'
        },
        'UnitsShown': {
            'description': '(free text)',
            'name': 'UnitsShown',
            'type': 'string'
        }
    },
    'type': 'object'
}
