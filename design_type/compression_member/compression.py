'''
Module : Compression member design

Author : Ashish Shitole

Reference :
               1) IS 800 : 2007 General construction in steel - Code of practice (Third revision)
               2) Design of Steel Structures by N. Subramanian

'''

from design_report.reportGenerator_latex import CreateLatex
from utils.common.Section_Properties_Calculator import *
from utils.common.component import *
# from cad.common_logic import CommonDesignLogic
from utils.common.material import *
from Report_functions import *
from utils.common.load import Load
from utils.common.Section_Properties_Calculator import *
from utils.common.is800_2007 import *

import logging
from design_type.member import Member



class Compression_bolted(Member):

    def __init__(self):
        super(Compression_bolted, self).__init__()
        self.design_status = False


    ###########################################
    # Design Preference Function Start
    ###########################################

    def tab_list(self):

        tabs = []

        t1 = (DISP_TITLE_ANGLE, TYPE_TAB_1, self.tab_angle_section)
        tabs.append(t1)

        t2 = (DISP_TITLE_CHANNEL, TYPE_TAB_1, self.tab_channel_section)
        tabs.append(t2)

        t3 = ("Connector", TYPE_TAB_2, self.plate_connector_values)
        tabs.append(t3)

        t4 = ("Detailing", TYPE_TAB_2, self.detailing_values)
        tabs.append(t4)

        t5 = ("Design", TYPE_TAB_2, self.design_values)
        tabs.append(t5)

        return tabs


    def tab_value_changed(self):

        change_tab = []

        t1 = (DISP_TITLE_ANGLE, [KEY_SECSIZE, KEY_SEC_MATERIAL,'Label_0'],
              [KEY_SECSIZE_SELECTED, KEY_SEC_FY, KEY_SEC_FU, 'Label_1', 'Label_2', 'Label_3', 'Label_4', 'Label_5',
               'Label_7', 'Label_8', 'Label_9',
               'Label_10', 'Label_11', 'Label_12', 'Label_13', 'Label_14', 'Label_15', 'Label_16', 'Label_17',
               'Label_18',
               'Label_19', 'Label_20', 'Label_21', 'Label_22', 'Label_23', 'Label_24', KEY_IMAGE], TYPE_TEXTBOX,
              self.get_new_angle_section_properties)
        change_tab.append(t1)


        t2 = (DISP_TITLE_ANGLE, ['Label_1', 'Label_2', 'Label_3','Label_0'],
              ['Label_7', 'Label_8', 'Label_9', 'Label_10', 'Label_11', 'Label_12', 'Label_13', 'Label_14', 'Label_15',
               'Label_16', 'Label_17', 'Label_18', 'Label_19', 'Label_20', 'Label_21', 'Label_22', 'Label_23',
               KEY_IMAGE],
              TYPE_TEXTBOX, self.get_Angle_sec_properties)
        change_tab.append(t2)

        t3 = (DISP_TITLE_CHANNEL, [KEY_SECSIZE, KEY_SEC_MATERIAL,'Label_0'],
              [KEY_SECSIZE_SELECTED, KEY_SEC_FY, KEY_SEC_FU, 'Label_1', 'Label_2', 'Label_3', 'Label_13', 'Label_14',
               'Label_4', 'Label_5',
               'Label_9', 'Label_10', 'Label_11', 'Label_12', 'Label_15', 'Label_16', 'Label_17',
               'Label_19', 'Label_20', 'Label_21',
               'Label_22', 'Label_23', 'Label_26','Label_27', KEY_IMAGE], TYPE_TEXTBOX, self.get_new_channel_section_properties)
        change_tab.append(t3)

        t4 = (DISP_TITLE_CHANNEL, ['Label_1', 'Label_2', 'Label_3', 'Label_13','Label_14'],
              ['Label_9', 'Label_10','Label_11', 'Label_12', 'Label_15',
               'Label_16', 'Label_17','Label_19', 'Label_20', 'Label_21', 'Label_22','Label_26','Label_27', KEY_IMAGE],
              TYPE_TEXTBOX, self.get_Channel_sec_properties)

        change_tab.append(t4)

        t5 = ("Connector", [KEY_CONNECTOR_MATERIAL], [KEY_CONNECTOR_FU, KEY_CONNECTOR_FY_20, KEY_CONNECTOR_FY_20_40,
                                                      KEY_CONNECTOR_FY_40], TYPE_TEXTBOX, self.get_fu_fy)
        change_tab.append(t5)

        t6 = (DISP_TITLE_ANGLE, [KEY_SECSIZE_SELECTED], [KEY_SOURCE], TYPE_TEXTBOX, self.change_source)
        change_tab.append(t6)

        t7 = (DISP_TITLE_CHANNEL, [KEY_SECSIZE_SELECTED], [KEY_SOURCE], TYPE_TEXTBOX, self.change_source)
        change_tab.append(t7)

        return change_tab


    def input_dictionary_design_pref(self):

        design_input = []


        t2 = (DISP_TITLE_ANGLE, TYPE_COMBOBOX, [KEY_SEC_MATERIAL])
        design_input.append(t2)

        t2 = (DISP_TITLE_CHANNEL, TYPE_COMBOBOX, [KEY_SEC_MATERIAL])
        design_input.append(t2)

        t5 = ("Detailing", TYPE_TEXTBOX, [KEY_DP_DETAILING_GAP])
        design_input.append(t5)

        t5 = ("Detailing", TYPE_COMBOBOX, [KEY_DP_DETAILING_CORROSIVE_INFLUENCES,KEY_DP_DETAILING_EDGE_TYPE])
        design_input.append(t5)

        t6 = ("Design", TYPE_COMBOBOX, [KEY_DP_DESIGN_METHOD])
        design_input.append(t6)

        t7 = ("Connector", TYPE_COMBOBOX, [KEY_CONNECTOR_MATERIAL])
        design_input.append(t7)

        return design_input


    def input_dictionary_without_design_pref(self):

        design_input = []

        t1 = (KEY_MATERIAL, [KEY_SEC_MATERIAL], 'Input Dock')
        design_input.append(t1)

        t2 = (None, [KEY_DP_DETAILING_EDGE_TYPE, KEY_DP_DETAILING_EDGE_TYPE, KEY_DP_DETAILING_GAP,
                     KEY_DP_DETAILING_CORROSIVE_INFLUENCES, KEY_DP_DESIGN_METHOD, KEY_CONNECTOR_MATERIAL], '')
        design_input.append(t2)

        return design_input


    def refresh_input_dock(self):

        add_buttons = []

        t2 = (DISP_TITLE_ANGLE, KEY_SECSIZE, TYPE_COMBOBOX_CUSTOMIZED, KEY_SECSIZE_SELECTED, KEY_SEC_PROFILE,
              ['Angles', 'Back to Back Angles', 'Star Angles'], "Angles")
        add_buttons.append(t2)

        t2 = (DISP_TITLE_CHANNEL, KEY_SECSIZE, TYPE_COMBOBOX_CUSTOMIZED, KEY_SECSIZE_SELECTED, KEY_SEC_PROFILE,
              ['Channels', 'Back to Back Channels'], "Channels")
        add_buttons.append(t2)

        return add_buttons

    ###################################
    # Design Preference Functions End
    ###################################


    def set_osdaglogger(key):
        global logger
        logger = logging.getLogger('Osdag')

        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        handler.setFormatter(formatter)
        logger.addHandler(handler)
        handler = logging.FileHandler('logging_text.log')

        formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if key is not None:
            handler = OurLog(key)
            formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
            handler.setFormatter(formatter)
            logger.addHandler(handler)


    def module_name(self):

        return KEY_DISP_COMPRESSION_BOLTED


    def customized_input(self):

        c_lst = []

        t1 = (KEY_SECSIZE, self.fn_profile_section)
        c_lst.append(t1)

        t2 = (KEY_GRD, self.grdval_customized)
        c_lst.append(t2)

        t3 = (KEY_D, self.diam_bolt_customized)
        c_lst.append(t3)

        return c_lst


    def fn_profile_section(self):

        profile = self[0]
        if profile == 'Beams':
            return connectdb("Beams", call_type="popup")
        elif profile == 'Columns':
            return connectdb("Columns", call_type= "popup")
        elif profile in ['Angles', 'Back to Back Angles', 'Star Angles']:
            return connectdb("Angles", call_type = "popup")
        elif profile in ['Channels', 'Back to Back Channels']:
            return connectdb("Channels", call_type = "popup")


    def input_value_changed(self):

        lst = []

        t1 = ([KEY_SEC_PROFILE], KEY_LOCATION, TYPE_COMBOBOX, self.fn_conn_type)
        lst.append(t1)

        t2 = ([KEY_SEC_PROFILE], KEY_SECSIZE, TYPE_COMBOBOX_CUSTOMIZED, self.fn_profile_section)
        lst.append(t2)

        t3 = ([KEY_SEC_PROFILE], KEY_IMAGE, TYPE_IMAGE, self.fn_conn_image)
        lst.append(t3)

        return lst


    def fn_conn_type(self):
        conn = self[0]
        if conn in ['Angles', 'Back to Back Angles', 'Star Angles']:
            return VALUES_LOCATION_1
        elif conn in ["Channels", "Back to Back Channels"]:
            return VALUES_LOCATION_2


    def fn_conn_image(self):
        img = self[0]
        if img == VALUES_SEC_PROFILE_2[0]:
            return VALUES_IMG_TENSIONBOLTED[0]
        elif img ==VALUES_SEC_PROFILE_2[1]:
            return VALUES_IMG_TENSIONBOLTED[1]
        elif img ==VALUES_SEC_PROFILE_2[2]:
            return VALUES_IMG_TENSIONBOLTED[2]
        elif img ==VALUES_SEC_PROFILE_2[3]:
            return VALUES_IMG_TENSIONBOLTED[3]
        else:
            return VALUES_IMG_TENSIONBOLTED[4]


    def input_values(self, existingvalues = {}):

        self.module = KEY_DISP_COMPRESSION_BOLTED
        self.mainmodule = 'Member'

        options_list = []

        t16 = (KEY_MODULE, KEY_DISP_COMPRESSION_BOLTED, TYPE_MODULE, None, True, 'No Validator')
        options_list.append(t16)

        t1 = (None, DISP_TITLE_CM, TYPE_TITLE, None, True, 'No Validator')
        options_list.append(t1)

        t2 = (KEY_SEC_PROFILE, KEY_DISP_SEC_PROFILE, TYPE_COMBOBOX, VALUES_SEC_PROFILE_2, True, 'No Validator')
        options_list.append(t2)

        t15 = (KEY_IMAGE, None, TYPE_IMAGE, VALUES_IMG_TENSIONBOLTED[0], True, 'No Validator')
        options_list.append(t15)

        t4 = (KEY_SECSIZE, KEY_DISP_SECSIZE, TYPE_COMBOBOX_CUSTOMIZED, ['All','Customized'], True, 'No Validator')
        options_list.append(t4)

        t5 = (KEY_MATERIAL, KEY_DISP_MATERIAL, TYPE_COMBOBOX, VALUES_MATERIAL, True, 'No Validator')
        options_list.append(t5)

        t5 = (KEY_LENGTH, KEY_DISP_LENGTH, TYPE_TEXTBOX, None, True, 'Int Validator')
        options_list.append(t5)

        t6 = (None, DISP_TITLE_FSL, TYPE_TITLE, None, True, 'No Validator')
        options_list.append(t6)

        t7 = (KEY_LOAD, KEY_DISP_LOAD_STAR, TYPE_TEXTBOX, None, True, 'Int Validator')
        options_list.append(t7)

        t8 = (KEY_LOAD_TYPE, KEY_DISP_LOAD_TYPE, TYPE_COMBOBOX_CUSTOMIZED, ['Axial', 'Non-Axial'], True, 'No Validator')
        options_list.append(t8)

        t9 = (KEY_END_1_TRANS, KEY_DISP_END_1_TRANS, TYPE_COMBOBOX_CUSTOMIZED, ['Free', 'Restrained'], True, 'No Validator')
        options_list.append(t9)

        t10 = (KEY_END_2_TRANS, KEY_DISP_END_2_TRANS, TYPE_COMBOBOX_CUSTOMIZED, ['Free', 'Restrained'], True, 'No Validator')
        options_list.append(t10)

        t11 = (KEY_END_1_ROT, KEY_DISP_END_1_ROT, TYPE_COMBOBOX_CUSTOMIZED, ['Free', 'Restrained'], True, 'No Validator')
        options_list.append(t11)

        t12 = (KEY_END_2_ROT, KEY_DISP_END_2_ROT, TYPE_COMBOBOX_CUSTOMIZED, ['Free', 'Restrained'], True, 'No Validator')
        options_list.append(t12)

        t13 = (KEY_NO_OF_BOLTS, KEY_DISP_NO_OF_BOLTS, TYPE_COMBOBOX_CUSTOMIZED, ['>= 2', '1'], True, 'No Validator')
        options_list.append(t13)

        t14 = (KEY_END, KEY_DISP_END, TYPE_COMBOBOX_CUSTOMIZED, ['fixed', 'hinged'], True, 'No Vaalidator')
        options_list.append(t14)

        return options_list


    def output_values(self, flag):

        out_list = []

        t1 = (None, DISP_TITLE_COMPRESSION_SECTION, TYPE_TITLE, None, True)
        out_list.append(t1)

        t2 = (KEY_DESIGNATION, KEY_DISP_DESIGNATION, TYPE_TEXTBOX,
              self.section_size_1.designation if flag else '', True)
        out_list.append(t2)

        t3 = (KEY_COMPRESSION_CAPACITY, KEY_DISP_COMPRESSION_CAPACITY, TYPE_TEXTBOX, round((self.section_size_1.compression_capacity_calc/1000),2) if flag else '', True)
        out_list.append(t3)

        t4 = (KEY_SLENDER, KEY_DISP_SLENDER, TYPE_TEXTBOX,
              self.section_size_1.slenderness if flag else '', True)
        out_list.append(t4)

        t5 = (KEY_EFFICIENCY, KEY_DISP_EFFICIENCY, TYPE_TEXTBOX,
              self.efficiency if flag else '', True)
        out_list.append(t5)

        return out_list


    def func_for_validation(self, design_dictionary):

        all_errors = []
        "check valid inputs and empty inputs in input dock"

        self.design_status = False

        flag = False
        flag1 = False
        flag2 = False
        # self.include_status = True

        option_list = self.input_values(self)
        missing_fields_list = []

        for option in option_list:
            if option[2] == TYPE_TEXTBOX:
                if design_dictionary[option[0]] == '':
                    missing_fields_list.append(option[1])
                else:
                    if option[2] == TYPE_TEXTBOX and option[0] == KEY_LENGTH:
                        # val = option[4]
                        # print(design_dictionary[option[0]], "jhvhj")
                        if float(design_dictionary[option[0]]) <= 0.0:
                            error = "Input value(s) cannot be equal or less than zero."
                            all_errors.append(error)
                        else:
                            flag1 = True

                    if option[2] == TYPE_TEXTBOX and option[0] == KEY_AXIAL:

                        if float(design_dictionary[option[0]]) <= 0.0:
                            error = "Input value(s) cannot be equal or less than zero."
                            all_errors.append(error)
                        else:
                            flag2 = True
            else:
                pass


        if len(missing_fields_list) > 0:
            error = self.generate_missing_fields_error_string(self, missing_fields_list)
            all_errors.append(error)
            # flag = False
        else:
            flag = True
        # print (all_errors,"ysdgh")
        # print (flag,flag1,flag2)
        if flag  and flag1 and flag2:
            self.set_input_values(self, design_dictionary)
            # print(design_dictionary)
        else:
            return all_errors


    def warn_text(self):
        """
        Function to give logger warning when any old value is selected from Column and Beams table.
        """
        global logger
        red_list = red_list_function()
        if self.supported_section.designation in red_list or self.supporting_section.designation in red_list:
            logger.warning(
            " : You are using a section (in red color) that is not available in latest version of IS 808")
            logger.info(
            " : You are using a section (in red color) that is not available in latest version of IS 808")


    def set_input_values(self, design_dictionary):


        super(Compression_bolted, self).set_input_values(self, design_dictionary)
        self.module = design_dictionary[KEY_MODULE]
        self.sizelist = design_dictionary[KEY_SECSIZE]
        self.sec_profile = design_dictionary[KEY_SEC_PROFILE]

        self.main_material = design_dictionary[KEY_MATERIAL]
        self.material = design_dictionary[KEY_SEC_MATERIAL]

        self.length = float(design_dictionary[KEY_LENGTH])

        self.load = Load(shear_force="", axial_force=design_dictionary.get(KEY_LOAD))
        self.efficiency = 0.0

        self.count = 0
        self.member_design_status = False
        self.max_limit_status_1 = False
        self.max_limit_status_2 = False

        print("The input values are set. Performing preliminary member check(s).")

        self.initial_member_capacity(self, design_dictionary)


    def select_section(self, design_dictionary, selectedsize):


        if design_dictionary[KEY_SEC_PROFILE] in ['Angles', 'Back to Back Angles', 'Star Angles']:
            self.section_size = Angle(designation=selectedsize, material_grade=design_dictionary[KEY_SEC_MATERIAL])
        elif design_dictionary[KEY_SEC_PROFILE] in ['Channels', 'Back to Back Channels']:
            self.section_size = Channel(designation=selectedsize, material_grade=design_dictionary[KEY_SEC_MATERIAL])
        else:
            pass

        return self.section_size


    def max_section(self, design_dictionary, sizelist):


        sec_area = {}
        sec_gyr = {}
        sec_depth = []

        for section in sizelist:
            if design_dictionary[KEY_SEC_PROFILE] in ['Angles']:
                self.section = Angle(designation=section, material_grade=design_dictionary[KEY_SEC_MATERIAL])
                self.min_rad_gyration_calc(self,designation=section, material_grade=design_dictionary[KEY_SEC_MATERIAL], key=design_dictionary[KEY_SEC_PROFILE],
                                                            subkey=design_dictionary[KEY_LOCATION],D_a=self.section.a,B_b=self.section.b,T_t=self.section.thickness)
                sec_gyr[self.section.designation] = self.min_radius_gyration
                if self.loc == "Long Leg":
                    sec_depth.append(self.section.max_leg)
                else:
                    sec_depth.append(self.section.min_leg)

            elif design_dictionary[KEY_SEC_PROFILE] in ['Back to Back Angles', 'Star Angles']:
                self.section = Angle(designation=section, material_grade=design_dictionary[KEY_SEC_MATERIAL])
                self.min_rad_gyration_calc(self,designation=section, material_grade=design_dictionary[KEY_SEC_MATERIAL],
                                           key=design_dictionary[KEY_SEC_PROFILE],
                                           subkey=design_dictionary[KEY_LOCATION], D_a=self.section.a,
                                           B_b=self.section.b, T_t=self.section.thickness)

                sec_gyr[self.section.designation] = self.min_radius_gyration
                if self.loc == "Long Leg":
                    sec_depth.append(self.section.max_leg)
                else:
                    sec_depth.append(self.section.min_leg)

            else:
                self.section = Channel(designation=section, material_grade=design_dictionary[KEY_SEC_MATERIAL])
                self.min_rad_gyration_calc(self,designation=section, material_grade=design_dictionary[KEY_SEC_MATERIAL],
                                           key=design_dictionary[KEY_SEC_PROFILE],
                                           subkey=design_dictionary[KEY_LOCATION], D_a=self.section.depth,
                                           B_b=self.section.flange_width, T_t=self.section.flange_thickness,t = self.section.web_thickness)
                sec_gyr[self.section.designation] = self.min_radius_gyration
                sec_depth.append(self.section.depth)
            sec_area[self.section.designation] = self.section.area

        print(sec_gyr)
        if len(sec_area) >= 2:
            self.max_area = max(sec_area, key=sec_area.get)
        else:
            self.max_area = self.section.designation

        if len(sec_gyr) >= 2:
            self.max_gyr = max(sec_gyr, key=sec_gyr.get)
        else:
            self.max_gyr = self.section.designation

        if len(sec_depth) >= 2:
            self.depth_max = max(sec_depth)
        else:
            self.depth_max = max(sec_depth)

        return self.max_area, self.max_gyr, self.depth_max


    def max_force_length(self, section):


        if self.sec_profile == 'Angles':


            self.section_size_max = Angle(designation=section, material_grade=self.material)
            self.section_size_max.compression_member_capacity(A_g=(self.section_size_max.area),
                                                  F_y=self.section_size_max.fy)
            self.max_member_force = self.section_size_max.compression_member_capacity
            self.min_rad_gyration_calc(self, designation=section, material_grade=self.material,
                               key=self.sec_profile, subkey=self.loc, D_a=self.section_size_max.a,
                               B_b=self.section_size_max.b, T_t=self.section_size_max.thickness)
            self.max_length = 180 * self.min_radius_gyration

        elif self.sec_profile in ['Back to Back Angles', 'Star Angles']:
            self.section_size_max = Angle(designation=section, material_grade=self.material)
            self.section_size_max.compression_member_capacity(A_g=(2 * self.section_size_max.area),
                                                  F_y=self.section_size_max.fy)
            # self.max_member_force = self.section_size_max.tension_yielding_capacity * 2
            self.min_rad_gyration_calc(self, designation=section, material_grade=self.material,
                               key=self.sec_profile, subkey=self.loc, D_a=self.section_size_max.a,
                               B_b=self.section_size_max.b, T_t=self.section_size_max.thickness)
            self.max_length = 180 * self.min_radius_gyration

        elif self.sec_profile == 'Channels':
            self.section_size_max = Channel(designation=section, material_grade=self.material)
            self.section_size_max.compression_member_capacity(A_g=(self.section_size_max.area),
                                                  F_y=self.section_size_max.fy)

            self.max_member_force = self.section_size_max.tension_yielding_capacity
            self.min_rad_gyration_calc(self, designation=section, material_grade=self.material,
                               key=self.sec_profile, subkey=self.loc, D_a=self.section_size_max.depth,
                               B_b=self.section_size_max.flange_width, T_t=self.section_size_max.flange_thickness,
                               t=self.section_size_max.web_thickness)
            self.max_length = 180 * self.min_radius_gyration


        elif self.sec_profile == 'Back to Back Channels':
            self.section_size_max = Channel(designation=section, material_grade=self.material)
            self.section_size_max.compression_member_capacity(A_g=(2 * self.section_size_max.area),
                                                  F_y=self.section_size_max.fy)
            # self.max_member_force = 2 * self.section_size_max.tension_yielding_capacity
            self.min_rad_gyration_calc(self, designation=section, material_grade=self.material,
                               key=self.sec_profile, subkey=self.loc, D_a=self.section_size_max.depth,
                               B_b=self.section_size_max.flange_width, T_t=self.section_size_max.flange_thickness,
                               t=self.section_size_max.web_thickness)
            self.max_length = 180 * self.min_radius_gyration
        self.section_size_max.design_check_for_slenderness(K=self.K, L=self.length,
                                                   r=self.min_radius_gyration)

        return self.section_size_max.compression_capacity, self.max_length, self.section_size_max.slenderness, self.min_radius_gyration


    def min_rad_gyration_calc(self,designation, material_grade,key,subkey, D_a=0.0,B_b=0.0,T_t=0.0,t=0.0):


        if key == "Channels" and subkey == "Web":
            Channel_attributes = Channel(designation, material_grade)
            rad_y = Channel_attributes.rad_of_gy_y
            rad_z = Channel_attributes.rad_of_gy_z
            min_rad = min(rad_y, rad_z)

        elif key == 'Back to Back Channels' and subkey == "Web":
            BBChannel_attributes = BBChannel_Properties()
            BBChannel_attributes.data(designation, material_grade)
            rad_y = BBChannel_attributes.calc_RogY(f_w=B_b, f_t=T_t, w_h=D_a, w_t=t) * 10
            rad_z = BBChannel_attributes.calc_RogZ(f_w=B_b, f_t=T_t, w_h=D_a, w_t=t) * 10
            min_rad = min(rad_y, rad_z)

        elif key == "Back to Back Angles" and subkey == 'Long Leg':
            BBAngle_attributes = BBAngle_Properties()
            BBAngle_attributes.data(designation, material_grade)
            rad_y = BBAngle_attributes.calc_RogY(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            rad_z = BBAngle_attributes.calc_RogZ(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            min_rad = min(rad_y, rad_z)

        elif key == 'Back to Back Angles' and subkey == 'Short Leg':
            BBAngle_attributes = BBAngle_Properties()
            BBAngle_attributes.data(designation, material_grade)
            rad_y = BBAngle_attributes.calc_RogY(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            rad_z = BBAngle_attributes.calc_RogZ(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            min_rad = min(rad_y, rad_z)

        elif key == 'Star Angles' and subkey == 'Long Leg':
            SAngle_attributes = SAngle_Properties()
            SAngle_attributes.data(designation, material_grade)
            rad_y = SAngle_attributes.calc_RogY(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            rad_z = SAngle_attributes.calc_RogZ(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            rad_u = SAngle_attributes.calc_RogU(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            rad_v = SAngle_attributes.calc_RogV(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            min_rad = min(rad_y, rad_z, rad_u, rad_v)

        elif key == 'Star Angles' and subkey == 'Short Leg':
            SAngle_attributes = SAngle_Properties()
            SAngle_attributes.data(designation, material_grade)
            rad_y = SAngle_attributes.calc_RogY(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            rad_z = SAngle_attributes.calc_RogZ(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            rad_u = SAngle_attributes.calc_RogU(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            rad_v = SAngle_attributes.calc_RogV(a=D_a, b=B_b, t=T_t, l=subkey) * 10
            min_rad = min(rad_y, rad_z, rad_u, rad_v)

        elif key == 'Angles' and (subkey == 'Long Leg' or subkey == 'Short Leg'):
            Angle_attributes = Angle(designation, material_grade)
            rad_u = Angle_attributes.rad_of_gy_u
            rad_v = Angle_attributes.rad_of_gy_v
            min_rad = min(rad_u, rad_v)

        self.min_radius_gyration = min_rad


    def initial_member_capacity(self,design_dictionary,previous_size = None):


        min_yield = 0

        if self.count == 0:
            self.max_section(self,design_dictionary,self.sizelist)
            [self.force1, self.len1, self.slen1, self.gyr1]= self.max_force_length(self,  self.max_area)
            [self.force2, self.len2, self.slen2, self.gyr2] = self.max_force_length(self,  self.max_gyr)
        else:
            pass

        self.count = self.count + 1
        "Loop checking each member from sizelist based on yield capacity"
        if (previous_size) == None:
            pass
        else:
            if previous_size in self.sizelist:
                self.sizelist.remove(previous_size)
            else:
                pass


        for selectedsize in self.sizelist:

            self.section_size = self.select_section(self,design_dictionary,selectedsize)

            if design_dictionary[KEY_SEC_PROFILE] =='Channels':
                self.cross_area = self.section_size.area

            elif design_dictionary[KEY_SEC_PROFILE] == 'Back to Back Channels':
                self.cross_area = self.section_size.area * 2

            elif design_dictionary[KEY_SEC_PROFILE] =='Angles':
                self.cross_area = self.section_size.area

            else:
                self.cross_area = self.section_size.area * 2


            self.section_size.compression_capacity(self, design_dictionary, Pd_1=self.section_size.compression_member_capacity_conc, Pd_2=self.section_size.compression_member_capacity_nonconc)
            self.section_size.effective_length
            # print(self.section_size.rad_of_gy_z)
            if design_dictionary[KEY_SEC_PROFILE] in ['Angles','Star Angles','Back to Back Angles']:
                # print(selectedsize)
                self.min_rad_gyration_calc(self,designation=self.section_size.designation, material_grade=self.material,
                                           key=self.sec_profile, subkey=self.loc, D_a=self.section_size.a,
                                           B_b=self.section_size.b, T_t=self.section_size.thickness)
            else:
                self.min_rad_gyration_calc(self,designation=self.section_size.designation, material_grade=self.material,
                                           key=self.sec_profile, subkey=self.loc, D_a=self.section_size.depth,
                                           B_b=self.section_size.flange_width, T_t=self.section_size.flange_thickness,
                                           t=self.section_size.web_thickness)
            self.section_size.design_check_for_slenderness(K=self.effective_length, L=design_dictionary[KEY_LENGTH],r=self.min_radius_gyration)


            if (self.section_size.compression_capacity >= self.load.axial_force*1000) and self.section_size.slenderness < 180:
                min_yield_current = self.section_size.compression_capacity
                self.member_design_status = True
                if min_yield == 0:
                    min_yield = min_yield_current
                    self.section_size_1 = self.select_section(self, design_dictionary, selectedsize)
                    self.section_size_1.compression_capacity(self, design_dictionary, Pd_1=self.section_size.compression_member_capacity_conc, Pd_2=self.section_size.compression_member_capacity_nonconc)
                    if design_dictionary[KEY_SEC_PROFILE] in ['Angles', 'Star Angles', 'Back to Back Angles']:
                        self.min_rad_gyration_calc(self,designation=self.section_size_1.designation,
                                                   material_grade=self.material,
                                                   key=self.sec_profile, subkey=self.loc, D_a=self.section_size_1.a,
                                                   B_b=self.section_size_1.b, T_t=self.section_size_1.thickness)

                    else:
                        self.min_rad_gyration_calc(self,designation=self.section_size_1.designation,
                                                   material_grade=self.material,
                                                   key=self.sec_profile, subkey=self.loc, D_a=self.section_size_1.depth,
                                                   B_b=self.section_size_1.flange_width,
                                                   T_t=self.section_size_1.flange_thickness,
                                                   t=self.section_size_1.web_thickness)

                    self.section_size_1.design_check_for_slenderness(K=self.effective_length, L=design_dictionary[KEY_LENGTH],
                                                               r=self.min_radius_gyration)

                elif min_yield_current < min_yield:
                    min_yield = min_yield_current
                    self.section_size_1 = self.select_section(self, design_dictionary, selectedsize)
                    self.section_size_1.compression_capacity(self, design_dictionary, Pd_1=self.section_size.compression_member_capacity_conc, Pd_2=self.section_size.compression_member_capacity_nonconc)
                    if design_dictionary[KEY_SEC_PROFILE] in ['Angles', 'Star Angles', 'Back to Back Angles']:
                        self.min_rad_gyration_calc(self,designation=self.section_size_1.designation,
                                                   material_grade=self.material,
                                                   key=self.sec_profile, subkey=self.loc, D_a=self.section_size_1.a,
                                                   B_b=self.section_size_1.b, T_t=self.section_size_1.thickness)
                    else:
                        self.min_rad_gyration_calc(self,designation=self.section_size_1.designation,
                                                   material_grade=self.material,
                                                   key=self.sec_profile, subkey=self.loc, D_a=self.section_size_1.depth,
                                                   B_b=self.section_size_1.flange_width,
                                                   T_t=self.section_size_1.flange_thickness,
                                                   t=self.section_size_1.web_thickness)
                self.section_size_1.design_check_for_slenderness(K=self.effective_length, L=design_dictionary[KEY_LENGTH],
                                                                 r=self.min_radius_gyration)

                # print(self.section_size_1.slenderness)


            elif (self.load.axial_force*1000 > self.force1) :
                self.max_limit_status_1 = True
                # self.design_status = False
                logger.warning(" : The factored tension force ({} kN) exceeds the tension capacity ({} kN) with respect to the maximum available "
                               "member size {}.".format(round(self.load.axial_force,2),round(self.force1/1000,2),self.max_area))
                logger.info(" : Define member(s) with a higher cross sectional area.")
                # logge r.error(": Design is not safe. \n ")
                # logger.info(" :=========End Of design===========")
                break


            elif self.length > self.len2:
                self.max_limit_status_2 = True
                # self.design_status = False
                logger.warning(" : The member length ({} mm) exceeds the maximum allowable length ({} mm) with respect to the maximum available "
                               "member size {}.".format(self.length,round(self.len2,2),self.max_gyr))
                logger.info(" : Select member(s) with a higher radius of gyration value.")
                # logger.error(": Design is not safe. \n ")
                # logger.info(" :=========End Of design===========")
                break

            else:
                pass

        if self.member_design_status == False and self.max_limit_status_1!=True and self.max_limit_status_2!=True:
            logger.warning(" : The available depth of the member cannot accommodate the minimum available bolt diameter of {} mm considering the "
                           "minimum spacing limit [Ref. Cl. 10.2, IS 800:2007].".format(self.bolt_diameter_min))
            logger.info(" : Reduce the bolt diameter or increase the member depth and re-design.")
            # logger.error(": Design is not safe. \n ")
            # logger.info(" :=========End Of design===========")

        if self.member_design_status == True:
            print("pass")
            self.design_status = True
            self.select_bolt_dia(self, design_dictionary)
        else:
            self.design_status = False
            logger.error(": Design is unsafe. \n ")
            logger.info(" :=========End Of design===========")


    def epsilon(self, fy):

        epsil = (250/fy)**0.5

        self.epsilon_value = round(epsil, 2)


    def k1_k2_k3(self, design_dictionary):

        no_of_bolts = design_dictionary[KEY_NO_OF_BOLTS]
        end = design_dictionary[KEY_END]
        # finding the values of k1, k2 and k3
        if no_of_bolts >= 2:
            if end == 'fixed':
                k1 = 0.20
                k2 = 0.35
                k3 = 20
            elif end == 'hinged':
                k1 = 0.70
                k2 = 0.60
                k3 = 5
        elif no_of_bolts == 1:
            if end == 'fixed':
                k1 = 0.75
                k2 = 0.35
                k3 = 20
            elif end == 'hinged':
                k1 = 1.25
                k2 = 0.50
                k3 = 60 
                
        return k1, k2, k3 


    def comprssion_member_capacity_conc(self, fy, alpha, design_dictionary):

        self.section_size = design_dictionary[KEY_SECSIZE]

        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        E = 2 * (10**5)
        fcc_value = (((math.pi)**2)*E)/((self.section_size.slenderness)**2)
        lambda_value = (fy / fcc_value)**0.5
        phi_value = 0.5*(1 + (alpha*(lambda_value - 0.2)) + ((lambda_value)**2))

        fcd_1 = (fy / gamma_m0)/(phi_value + (((phi_value)**2 - (lambda_value)**2)**0.5))
        Pd_1 = fcd_1 * (self.section_size.area)

        self.compression_capacity_conc = round(Pd_1, 2)


    def compression_member_capacity_nonconc(self, fy, alpha, design_dictionary):

        self.section_size = design_dictionary[KEY_SECSIZE]
        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']
        

        # Finding the value of lambda_e

        b1 = self.section_size.a 
        b2 = self.section_size.b
        t = self.section_size.thickness

        eps = self.section_size.epsilon
        lambda_vv = (self.section_size.slenderness)/(eps*(((math.pi)**2)*eps/250)**0.5)
        lambda_phi = ((b1 + b2)/2*t)/(eps*(((math.pi)**2)*eps/250)**0.5)

        lambda_e = (k1 + (k2 * ((lambda_vv)**2)) + (k3 * ((lambda_phi)**2)))**0.5

        # finding the compression capacity
        phi_value = 0.5 * (1 + (self.section_size.alpha * (lambda_e - 0.2)) + ((lambda_e) ** 2))

        fcd_2 = (fy / gamma_m0) / (phi_value + (((phi_value) ** 2 - (lambda_e) ** 2) ** 0.5))
        Pd_2 = fcd_2 * (self.section_size.area)

        self.compression_capacity_nonconc = round(Pd_2, 2)


    def alpha(self, design_dictionary):

        if design_dictionary[KEY_SEC_PROFILE] in ['Angles', 'Back to Back Angles', 'Star Angles', 'Channels', 'Back to Back Channels']:
            Alp = 0.49

        self.alpha = Alp


    def compression_capacity_calc(self, design_dictionary, Pd_1, Pd_2):

        if design_dictionary[KEY_LOAD_TYPE] == 'Axial':
            C_c = Pd_1
        elif design_dictionary[KEY_LOAD_TYPE] == 'Non-Axial':
            C_c = Pd_2

        self.compression_capacity = C_c


    def effective_length(self, design_dictionary):

        if design_dictionary[KEY_END_1_TRANS] == 'restrained' and design_dictionary[KEY_END_1_ROT] == 'restrained':
            if design_dictionary[KEY_END_2_TRANS] == 'free' and design_dictionary[KEY_END_2_ROT] == 'free':
                k = 2.0
            elif design_dictionary[KEY_END_2_TRANS] == 'free' and design_dictionary[KEY_END_2_ROT] == 'restrained':
                k = 1.2
            elif design_dictionary[KEY_END_2_TRANS] == 'restrained' and design_dictionary[KEY_END_2_ROT] == 'free':
                k = 0.8
            elif design_dictionary[KEY_END_2_TRANS] == 'restrained' and design_dictionary[KEY_END_2_ROT] == 'restrained':
                k = 0.65
        elif design_dictionary[KEY_END_1_TRANS] == 'free' and design_dictionary[KEY_END_1_ROT] == 'restrained':
            if design_dictionary[KEY_END_2_TRANS] == 'free' and design_dictionary[KEY_END_2_ROT] == 'restrained':
                k = 2.0
        elif design_dictionary[KEY_END_1_TRANS] == 'restrained' and design_dictionary[KEY_END_1_ROT] == 'free':
            if design_dictionary[KEY_END_2_TRANS] == 'restrained' and design_dictionary[KEY_END_2_ROT] == 'free':
                k = 1.0

        return k


    def member_check(self, design_dictionary):


        if self.section_size.compression_capacity >= self.load.axial_force * 1000:
            self.design_status = True
            self.efficiency = round((self.load.axial_force * 1000 / self.section_size.compression_capacity), 2)


        else:
            if len(self.sizelist) >= 2:
                size = self.section_size_1.designation
                print("recheck", size)
                self.initial_member_capacity(self, design_dictionary, size)
            else:
                self.design_status = False
                logger.warning(
                 " : The factored tension force ({} kN) exceeds the tension capacity ({} kN) with respect to the maximum available "
                 "member size {}."
                 .format(round(self.load.axial_force, 2), round(self.section_size.compression_capacity / 1000, 2),
                    self.max_area))
                logger.info(" : Select member(s) with a higher cross sectional area.")
                logger.error(": Design is unsafe. \n ")
                logger.info(" :=========End Of design===========")


    def results_to_test(self, filename):

        test_out_list ={KEY_DISP_DESIGNATION:self.section_size_1.designation,
                         KEY_DISP_COMPRESSION_CAPACITY:self.section_size_1.compression_capacity,
                         KEY_DISP_SLENDER:self.section_size_1.slenderness,
                         KEY_DISP_EFFICIENCY:self.efficiency}

        f = open(filename, "w")
        f.write(str(test_out_list))
        f.close()


    def save_design(self, popup_summary):

        section_size = self.section_size_1
        if self.member_design_status == True:
            member_compression_capacity = round((section_size.compression_capacity / 1000), 2)
            slenderness = section_size.slenderness
            gyration = self.min_radius_gyration
        else:
            if self.max_limit_status_2 == True:
                [member_compression_capacity, l, slenderness, gyration] = self.max_force_length(self, self.max_gyr)
                member_compression_capacity = round(member_compression_capacity / 1000, 2)
            else:
                [member_compression_capacity, l, slenderness, gyration] = self.max_force_length(self, self.max_area)
                member_compression_capacity = round(member_compression_capacity / 1000, 2)

        # if self.member_design_status == True:
        if self.sec_profile == "Channels":
            self.report_supporting = {KEY_DISP_SEC_PROFILE: image,
                                      # Image shall be save with this name.png in resource files
                                      KEY_DISP_SECSIZE: (section_size.designation,self.sec_profile),
                                      KEY_DISP_MATERIAL: section_size.material,
                                      KEY_REPORT_MASS: round(section_size.mass,2),
                                      KEY_REPORT_AREA: round(section_size.area,2),
                                      KEY_REPORT_DEPTH: round(section_size.depth,2),
                                      KEY_REPORT_WIDTH: round(section_size.flange_width,2),
                                      KEY_REPORT_WEB_THK: round(section_size.web_thickness,2),
                                      KEY_REPORT_FLANGE_THK: round(section_size.flange_thickness,2),
                                      KEY_DISP_FLANGE_S_REPORT: round(section_size.flange_slope,2),
                                      KEY_REPORT_R1: round(section_size.root_radius,2),
                                      KEY_REPORT_R2:round(section_size.toe_radius,2),
                                      KEY_REPORT_CY: round(section_size.Cy,2),
                                      KEY_REPORT_IZ: round(section_size.mom_inertia_z * 1e-4,2),
                                      KEY_REPORT_IY: round(section_size.mom_inertia_y * 1e-4,2),
                                      KEY_REPORT_RZ: round(section_size.rad_of_gy_z * 1e-1,2),
                                      KEY_REPORT_RY: round(section_size.rad_of_gy_y * 1e-1,2),
                                      KEY_REPORT_ZEZ: round(section_size.elast_sec_mod_z * 1e-3,2),
                                      KEY_REPORT_ZEY: round(section_size.elast_sec_mod_y * 1e-3,2),
                                      KEY_REPORT_ZPZ: round(section_size.plast_sec_mod_z * 1e-3,2),
                                      KEY_REPORT_ZPY: round(section_size.elast_sec_mod_y * 1e-3,2),
                                      KEY_REPORT_RADIUS_GYRATION: round(gyration,2)}

            thickness = section_size.web_thickness
            text = "C"
        elif self.sec_profile == "Back to Back Channels":
            BBChannel =BBChannel_Properties()
            BBChannel.data(section_size.designation, section_size.material)
            self.report_supporting = {KEY_DISP_SEC_PROFILE: image,
                                      # Image shall be save with this name.png in resource files
                                      KEY_DISP_SECSIZE: (section_size.designation, self.sec_profile),
                                      KEY_DISP_MATERIAL: section_size.material,
                                      KEY_REPORT_MASS: round(2*section_size.mass, 2),
                                      KEY_REPORT_AREA: round(2*section_size.area, 2),
                                      KEY_REPORT_DEPTH: round(section_size.depth, 2),
                                      KEY_REPORT_WIDTH: round(section_size.flange_width, 2),
                                      KEY_REPORT_WEB_THK: round(section_size.web_thickness, 2),
                                      KEY_REPORT_FLANGE_THK: round(section_size.flange_thickness, 2),
                                      '$T_p$ (mm)': round(self.plate.thickness_provided, 2),
                                      KEY_DISP_FLANGE_S_REPORT: round(section_size.flange_slope, 2),
                                      KEY_REPORT_R1: round(section_size.root_radius, 2),
                                      KEY_REPORT_R2: round(section_size.toe_radius, 2),
                                      KEY_REPORT_IZ: round((BBChannel.calc_MomentOfAreaZ(section_size.flange_width,section_size.flange_thickness,section_size.depth,section_size.web_thickness)*10000) * 1e-4,2),
                                      KEY_REPORT_IY: round((BBChannel.calc_MomentOfAreaY(section_size.flange_width,section_size.flange_thickness,section_size.depth,section_size.web_thickness)*10000) * 1e-4,2),
                                      KEY_REPORT_RZ: round((BBChannel.calc_RogZ(section_size.flange_width,section_size.flange_thickness,section_size.depth,section_size.web_thickness)*10) * 1e-1,2),
                                      KEY_REPORT_RY: round((BBChannel.calc_RogY(section_size.flange_width,section_size.flange_thickness,section_size.depth,section_size.web_thickness)*10) * 1e-1,2),
                                      KEY_REPORT_ZEZ: round((BBChannel.calc_ElasticModulusZz(section_size.flange_width,section_size.flange_thickness,section_size.depth,section_size.web_thickness)*1000) * 1e-3,2),
                                      KEY_REPORT_ZEY: round((BBChannel.calc_ElasticModulusZy(section_size.flange_width,section_size.flange_thickness,section_size.depth,section_size.web_thickness)*1000) * 1e-3,2),
                                      KEY_REPORT_ZPZ: round((BBChannel.calc_PlasticModulusZpz(section_size.flange_width,section_size.flange_thickness,section_size.depth,section_size.web_thickness)*1000) * 1e-3,2),
                                      KEY_REPORT_ZPY: round((BBChannel.calc_PlasticModulusZpy(section_size.flange_width,section_size.flange_thickness,section_size.depth,section_size.web_thickness)*1000) * 1e-3,2),
                                      KEY_REPORT_RADIUS_GYRATION: round(gyration, 2)}
            thickness = section_size.web_thickness
            text = "C"

        elif self.sec_profile == "Angles":
            self.report_supporting = {KEY_DISP_SEC_PROFILE: image,
                                      # Image shall be save with this name.png in resource files
                                      KEY_DISP_SECSIZE: (section_size.designation,self.sec_profile),
                                      KEY_DISP_MATERIAL: section_size.material,
                                      KEY_REPORT_MASS: round(section_size.mass,2),
                                      KEY_REPORT_AREA: round((section_size.area),2),
                                      KEY_REPORT_MAX_LEG_SIZE: round(section_size.max_leg,2),
                                      KEY_REPORT_MIN_LEG_SIZE: round(section_size.min_leg,2),
                                      KEY_REPORT_ANGLE_THK: round(section_size.thickness,2),
                                      KEY_REPORT_R1: round(section_size.root_radius,2),
                                      KEY_REPORT_R2: round(section_size.toe_radius,2),
                                      KEY_REPORT_CY: round(section_size.Cy,2),
                                      KEY_REPORT_CZ: round(section_size.Cz,2),
                                      KEY_REPORT_IZ: round(section_size.mom_inertia_z * 1e-4,2),
                                      KEY_REPORT_IY: round(section_size.mom_inertia_y * 1e-4,2),
                                      KEY_REPORT_IU: round(section_size.mom_inertia_u * 1e-4,2),
                                      KEY_REPORT_IV: round(section_size.mom_inertia_v * 1e-4,2),
                                      KEY_REPORT_RZ: round(section_size.rad_of_gy_z * 1e-1,2),
                                      KEY_REPORT_RY: round((section_size.rad_of_gy_y) * 1e-1,2),
                                      KEY_REPORT_RU: round((section_size.rad_of_gy_u) * 1e-1,2),
                                      KEY_REPORT_RV: round((section_size.rad_of_gy_v) * 1e-1,2),
                                      KEY_REPORT_ZEZ: round(section_size.elast_sec_mod_z * 1e-3,2),
                                      KEY_REPORT_ZEY: round(section_size.elast_sec_mod_y * 1e-3,2),
                                      KEY_REPORT_ZPZ: round(section_size.plast_sec_mod_z * 1e-3,2),
                                      KEY_REPORT_ZPY: round(section_size.plast_sec_mod_y * 1e-3,2),
                                      KEY_REPORT_RADIUS_GYRATION: round(gyration,2)}
            thickness = section_size.thickness
            text = "A"

        elif self.sec_profile == "Back to Back Angles":
            Angle_attributes = BBAngle_Properties()
            Angle_attributes.data(section_size.designation,section_size.material)
            if self.loc == "Long Leg":
                Cz = round((Angle_attributes.calc_Cz(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)*10),2)
                Cy = "N/A"
            else:
                Cy = round((Angle_attributes.calc_Cy(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)*10),2)
                Cz = "N/A"

            self.report_supporting = {KEY_DISP_SEC_PROFILE: image,
                                      # Image shall be save with this name.png in resource files
                                      KEY_DISP_SECSIZE: (section_size.designation,self.sec_profile),
                                      KEY_DISP_MATERIAL: section_size.material,
                                      KEY_REPORT_MASS: round(2*section_size.mass,2),
                                      KEY_REPORT_AREA: round((2*section_size.area),2),
                                      KEY_REPORT_MAX_LEG_SIZE: round(section_size.max_leg,2),
                                      KEY_REPORT_MIN_LEG_SIZE: round(section_size.min_leg,2),
                                      KEY_REPORT_ANGLE_THK: round(section_size.thickness,2),
                                      '$T$ (mm)': round(self.plate.thickness_provided, 2),
                                      KEY_REPORT_R1: round(section_size.root_radius,2),
                                      KEY_REPORT_R2: round(section_size.toe_radius,2),
                                      KEY_REPORT_CY: Cy,
                                      KEY_REPORT_CZ: Cz,
                                      KEY_REPORT_IZ: round((Angle_attributes.calc_MomentOfAreaZ(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)*10000) * 1e-4,2),
                                      KEY_REPORT_IY: round((Angle_attributes.calc_MomentOfAreaY(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)*10000) * 1e-4,2),
                                      KEY_REPORT_IU: round((Angle_attributes.calc_MomentOfAreaY(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)*10000) * 1e-4,2),
                                      KEY_REPORT_IV: round((Angle_attributes.calc_MomentOfAreaZ(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)*10000) * 1e-4,2),
                                      KEY_REPORT_RZ: round((Angle_attributes.calc_RogZ(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)),2),
                                      KEY_REPORT_RY: round((Angle_attributes.calc_RogY(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)),2),
                                      KEY_REPORT_RU: round((Angle_attributes.calc_RogY(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)), 2),
                                      KEY_REPORT_RV: round((Angle_attributes.calc_RogZ(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)), 2),
                                      KEY_REPORT_ZEZ: round((Angle_attributes.calc_ElasticModulusZz(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)),2),
                                      KEY_REPORT_ZEY: round((Angle_attributes.calc_ElasticModulusZy(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)),2),
                                      KEY_REPORT_ZPZ: round((Angle_attributes.calc_PlasticModulusZpz(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)),2),
                                      KEY_REPORT_ZPY: round((Angle_attributes.calc_PlasticModulusZpy(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)),2),
                                      KEY_REPORT_RADIUS_GYRATION: round(gyration,2)}
            thickness = section_size.thickness
            text = "A"
        else:
            Angle_attributes = SAngle_Properties()
            Angle_attributes.data(section_size.designation, section_size.material)

            self.report_supporting = {KEY_DISP_SEC_PROFILE: image,
                                      # Image shall be save with this name.png in resource files
                                      KEY_DISP_SECSIZE: (section_size.designation, self.sec_profile),
                                      KEY_DISP_MATERIAL: section_size.material,
                                      KEY_REPORT_MASS: round(2*section_size.mass, 2),
                                      KEY_REPORT_AREA: round((2*section_size.area), 2),
                                      KEY_REPORT_MAX_LEG_SIZE: round(section_size.max_leg, 2),
                                      KEY_REPORT_MIN_LEG_SIZE: round(section_size.min_leg, 2),
                                      KEY_REPORT_ANGLE_THK: round(section_size.thickness, 2),
                                      '$T$ (mm)': round(self.plate.thickness_provided, 2),
                                      KEY_REPORT_R1: round(section_size.root_radius, 2),
                                      KEY_REPORT_R2: round(section_size.toe_radius, 2),
                                      KEY_REPORT_IZ: round((Angle_attributes.calc_MomentOfAreaZ(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)), 2),
                                      KEY_REPORT_IY: round((Angle_attributes.calc_MomentOfAreaY(section_size.max_leg, section_size.min_leg,section_size.thickness,self.loc)), 2),
                                      KEY_REPORT_IU: round((Angle_attributes.calc_MomentOfAreaU(section_size.max_leg,section_size.min_leg,section_size.thickness,self.loc)), 2),
                                      KEY_REPORT_IV: round((Angle_attributes.calc_MomentOfAreaV(section_size.max_leg,section_size.min_leg,section_size.thickness, self.loc)), 2),
                                      KEY_REPORT_RZ: round((Angle_attributes.calc_RogZ(section_size.max_leg, section_size.min_leg, section_size.thickness,self.loc)), 2),
                                      KEY_REPORT_RY: round((Angle_attributes.calc_RogY(section_size.max_leg, section_size.min_leg, section_size.thickness,self.loc)), 2),
                                      KEY_REPORT_RU: round((Angle_attributes.calc_RogU(section_size.max_leg,section_size.min_leg, section_size.thickness, self.loc)), 2),
                                      KEY_REPORT_RV: round((Angle_attributes.calc_RogV(section_size.max_leg,section_size.min_leg,section_size.thickness, self.loc)), 2),
                                      KEY_REPORT_ZEZ: round((Angle_attributes.calc_ElasticModulusZz(section_size.max_leg, section_size.min_leg, section_size.thickness,  self.loc)), 2),
                                      KEY_REPORT_ZEY: round((Angle_attributes.calc_ElasticModulusZy(section_size.max_leg, section_size.min_leg, section_size.thickness, self.loc)), 2),
                                      KEY_REPORT_ZPZ: round((Angle_attributes.calc_PlasticModulusZpz(section_size.max_leg, section_size.min_leg, section_size.thickness, self.loc)), 2),
                                      KEY_REPORT_ZPY: round((Angle_attributes.calc_PlasticModulusZpy(section_size.max_leg, section_size.min_leg, section_size.thickness,self.loc)), 2),
                                      KEY_REPORT_RADIUS_GYRATION: round(gyration, 2)}
            thickness = section_size.thickness
            text = "A"

        self.report_input = \
                {
                 KEY_MODULE : self.module,
                 KEY_DISP_LEGTH : self.length,
                 "Selected Section Details" : self.report_supporting,

                 KEY_DISP_SEC_PROFILE : self.sec_profile,
                 KEY_DISP_SECSIZE : str(self.sizelist),
                 "Section Material" : section_size.material,
                 KEY_DISP_ULTIMATE_STRENGTH_REPORT: round(section_size.fu, 2),
                 KEY_DISP_YIELD_STRENGTH_REPORT: round(section_size.fy, 2),

                 "Detailing - Design Preference": "TITLE",
                 KEY_DISP_DP_DETAILING_EDGE_TYPE: self.bolt.edge_type,
                 # 'Type of edges for edge distance': 'Machine flame cut',
                 # KEY_DISP_DP_DETAILING_GAP: self.plate.gap,
                 KEY_DISP_DP_DETAILING_CORROSIVE_INFLUENCES_BEAM: self.bolt.corrosive_influences}


        self.report_check = []

        gamma_m0 = IS800_2007.cl_5_4_1_Table_5["gamma_m0"]['yielding']

        if self.sec_profile in ["Back to Back Angles", "Star Angles", "Back to Back Channels"]:
            multiple = 2
        else:
            multiple =1

        t1 = ('Selected', 'Selected Member Data', '|p{5cm}|p{2cm}|p{2cm}|p{2cm}|p{4cm}|')
        self.report_check.append(t1)

        if self.member_design_status == True:
            t1 = ('SubSection', 'Parameters Check', '|p{2.5cm}|p{7.5cm}|p{3cm}|p{2.5cm}|')
            self.report_check.append(t1)

































