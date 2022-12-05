FACULTY_KEY = 'faculty'
FORM_KEY = 'form'
YEAR_KEY = 'year'
GROUP_KEY = 'group'

FACULTY_0 = 'faculty_of_IT'

# forms
FORM_0 = 'ochnaya'
FORM_1 = 'ochno-zaochnaya_vikhodnogo_dnya'
FORM_2 = 'zaochnaya_vikhodnogo_dnya'

# years of FORM_0
Y1_F0 = 'year_1_form_0'
Y2_F0 = 'year_2_form_0'
Y3_F0 = 'year_3_form_0'
Y1S_F0 = 'year_1spo_form_0'
Y2S_F0 = 'year_2spo_form_0'
Y3S_F0 = 'year_3spo_form_0'
Y4_F0 = 'year_4_form_0'

# groups of Y1_F0
G0_Y1_F0 = 'group_ID 30.1/B-22'
G1_Y1_F0 = 'group_ID 23.1/B-22'
# groups of Y2_F0
G0_Y2_F0 = 'group_o. ID 23.1/B-21'
G1_Y2_F0 = 'group_o. ID 23.2/B-21'
G2_Y2_F0 = 'group_o. ID 23.3/B-21'
G3_Y2_F0 = 'group_o. ID 23.4/B-21'
G4_Y2_F0 = 'group_o. ID 30.1/B-21'
# groups of Y3_F0
G0_Y3_F0 = 'group_ID 23.1/B1-20'
G1_Y3_F0 = 'group_ID 23.1/B2-20'
G2_Y3_F0 = 'group_ID 23.2/B2-20'
# groups of Y1S_F0
G0_Y1S_F0 = 'group_IDs 23.1/B-22'
# groups of Y2S_F0
G0_Y2S_F0 = 'group_o.IDs 23.1/B3-21'
# groups of Y3S_F0
G0_Y3S_F0 = 'group_IDs 23.1/B1-20'
# groups of Y4_F0
G0_Y4_F0 = 'group_ID 23.1/B1-19'
G1_Y4_F0 = 'group_ID 23.2/B1-19'
G2_Y4_F0 = 'group_ID 23.1/B2-19'

# years of FORM_1
Y1_F1 = 'year_1_form_1'
Y1S_F1 = 'year_1spo_form_1'
Y2S_F1 = 'year_2spo_form_1'

# groups of Y1_F1
G0_Y1_F1 = 'group_IVS 30.1/B-22'
# groups of Y1S_F1
G0_Y1S_F1 = 'group_IVSs 30.1/B-22'
# groups of Y2S_F1
G0_Y2S_F1 = 'group_o.IVSs 23.1/B-21'
G1_Y2S_F1 = 'group_o.IVSs 30.1/B-21'

# years of FORM_2
Y1S_F2 = 'year_1_form_2'
Y3S_F2 = 'year_3_form_2'
Y4S_F2 = 'year_4_form_2'

# groups of Y1S_F2
G0_Y1S_F2 = 'group_ISs 23.1/B-22'
G1_Y1S_F2 = 'group_ISs 23.2/B-22'
# groups of Y3S_F2
G0_Y3S_F2 = 'group_ISs 23.1/B1-20'
# groups of Y4S_F2
G0_Y4S_F2 = 'group_ISs 23.1/B1-19'

EVERYTHING = {FACULTY_0:
                  {FORM_0: {Y1_F0: {G0_Y1_F0: 'ИД 30.1/Б-22', G1_Y1_F0: 'ИД 23.1/Б-22'},
                            Y2_F0: {G0_Y2_F0: 'о. ИД 23.1/Б-21', G1_Y2_F0: 'о. ИД 23.2/Б-21',
                                    G2_Y2_F0: 'о. ИД 23.3/Б-21', G3_Y2_F0: 'о. ИД 23.4/Б-21',
                                    G4_Y2_F0: 'о. ИД 30.1/Б-21'},
                            Y3_F0: {G0_Y3_F0: 'ИД 23.1/Б1-20', G1_Y3_F0: 'ИД 23.1/Б2-20',
                                    G2_Y3_F0: 'ИД 23.2/Б2-20'},

                            Y1S_F0: {G0_Y1S_F0: 'ИДс 23.1/Б-22'},
                            Y2S_F0: {G0_Y2S_F0: 'о.ИДс 23.1/Б3-21'},
                            Y3S_F0: {G0_Y3S_F0: 'ИДс 23.1/Б1-20'},

                            Y4_F0: {G0_Y4_F0: 'ИД 23.1/Б1-19', G1_Y4_F0: 'ИД 23.2/Б1-19',
                                    G2_Y4_F0: 'ИД 23.1/Б2-19'}},

                   FORM_1: {Y1_F1: {G0_Y1_F1: 'ИВС 30.1/Б-22'},
                            Y1S_F1: {G0_Y1S_F1: 'ИВСс 30.1/Б-22'},
                            Y2S_F1: {G0_Y2S_F1: 'ИВСс 23.1/Б-21', G1_Y2S_F1: 'ИВСс 30.1/Б-21'}},

                   FORM_2: {Y1S_F2: {G0_Y1S_F2: 'ИСс 23.1/Б-22', G1_Y1S_F2: 'ИСс 23.2/Б-22'},
                            Y3S_F2: {G0_Y3S_F2: 'ИСс 23.1/Б1-20'},
                            Y4S_F2: {G0_Y4S_F2: 'ИСс 23.1/Б1-19'}}
                   }
              }
