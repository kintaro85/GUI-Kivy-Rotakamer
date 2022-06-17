import csv
from logging import fatal, logThreads
from typing import Text
from kivy import event
from kivy.app import App
from kivy.core import image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

class Staff(Widget):
    def __init__(self, name,**kwargs):
        super().__init__(**kwargs)
        self.name = name
        #self.staffType = staffType 

        self.split = Button(text = "split", bold = True,background_color = '#87a18a')
        self.tenf = Button(text = "10-5", bold = True,background_color = '#87a18a')
        self.twel = Button(text = "12-11", bold = True,background_color = '#87a18a')
        self.tre = Button(text = "3-f", bold = True,background_color = '#87a18a')
        self.hol = Button(text = "holiday", bold = True,background_color = '#87a18a')
        self.off = Button(text = "off", bold = True,background_color = '#87a18a')

        self.split.bind(on_press = self.change_btn_color)
        self.tenf.bind(on_press = self.change_btn_color)
        self.twel.bind(on_press = self.change_btn_color)
        self.tre.bind(on_press = self.change_btn_color)
        self.hol.bind(on_press = self.change_btn_color)
        self.off.bind(on_press = self.change_btn_color)
        
        self.split.bind(on_press = self.addshift_to_mustdo)
        self.tenf.bind(on_press = self.addshift_to_mustdo)
        self.twel.bind(on_press = self.addshift_to_mustdo)
        self.tre.bind(on_press = self.addshift_to_mustdo)
        self.hol.bind(on_press = self.addshift_to_mustdo)
        self.off.bind(on_press = self.addshift_to_mustdo)

        self.staf_on_off = Button(text = f"{self.name}",background_color = '#87a18a')
        self.staf_on_off.bind(on_press = self.turnStaff_on_off)
        
        self.sactive = False

        self.newlin = '\n'

        self.addshift = Button(text = "View List", bold = True,background_color = '#87a18a',font_size = 10)
        self.addshift.bind(on_press = self.add_mustto_tolabel)
        

        self.mustdolabel =  Label(text = '',font_size='11sp')
        
        self.staflabel = Label(text = self.name)
        
        self.endlist_label =  Label(text = "end list:")

        self.delete_butt = Button(text = "delete", bold = True,background_color = '#87a18a',font_size = 10)
        self.delete_butt.bind(on_press = self.delete)
        

        self.listof_mustdo = []
        #self.endlist_labe = Label(text = "")
        self.end_list = [self.name," ","off ","off ","off ","off ","off "]
        self.end_list_shift = [self.name]


        self.s_counter = 0
        self.t_counter = 0
        self.tw_counter = 0
        self.tr_counter = 0
        self.hl_counter = 0

        self.sp_counter = 0
        self.te_counter = 0
        self.twe_counter = 0
        self.tre_counter = 0

        self.sat_is_empty = True
        self.tue_is_empty = True
        self.wed_is_empty = True
        self.thu_is_empty = True
        self.fri_is_empty = True
        
        self.isfilling = True 

    def turnStaff_on_off(self,event):
        if self.sactive == False:
            self.sactive = True
            event.background_color = '#0e630f'
        elif self.sactive == True:
            self.sactive = False
            event.background_color = '#87a18a'
        print(event.text)
        print(self.sactive)
        
    
    

    def delete(self,event):
        self.listof_mustdo.pop()

    def change_btn_color(self,event):
        sp = []
        te = []
        tw = []
        tr = []
        hl = []
        
        a = self.listof_mustdo
        for n in a:
            if n == "a split":
                sp.append("s")
            elif n == "b 10-5":
                te.append("te")
            elif n == "c 12-11":
                tw.append("tw")
            elif n == "d 3-f":
                tr.append("tr")
            elif n == "e holiday":
                hl.append("hl")
        splen = len(sp)
        telen = len(te)
        twlen = len(tw)
        trlen = len(tr)
        hllen = len(hl)
        
        if event.text == "split":
            if splen == 0:
                event.background_color = '#87a18a'
            elif splen == 1:
                event.background_color = '#10b326'
            elif splen == 2:
                event.background_color = 'fff833'
            elif splen == 3:
                event.background_color = '#ff2200'
            elif splen == 4:
                event.background_color = '#5c0313'
            elif splen == 5:
                event.background_color = '#2e0109'
        
        if event.text == "10-5":
            if telen == 0:
                event.background_color = '#87a18a'
            elif telen == 1:
                event.background_color = '#10b326'
            elif telen == 2:
                event.background_color = 'fff833'
            elif telen == 3:
                event.background_color = '#ff2200'
            elif telen == 4:
                event.background_color = '#5c0313'
            elif telen == 5:
                event.background_color = '#2e0109'

        if event.text == "12-11":
            if twlen == 0:
                event.background_color = '#87a18a'
            elif twlen == 1:
                event.background_color = '#10b326'
            elif twlen == 2:
                event.background_color = 'fff833'
            elif twlen == 3:
                event.background_color = '#ff2200'
            elif twlen == 4:
                event.background_color = '#5c0313'
            elif twlen == 5:
                event.background_color = '#2e0109'
        
        if event.text == "3-f":
            if trlen == 0:
                event.background_color = '#87a18a'
            elif trlen == 1:
                event.background_color = '#10b326'
            elif trlen == 2:
                event.background_color = 'fff833'
            elif trlen == 3:
                event.background_color = '#ff2200'
            elif trlen == 4:
                event.background_color = '#5c0313'
            elif trlen == 5:
                event.background_color = '#2e0109'
        
        if event.text == "holiday":
            if hllen == 0:
                event.background_color = '#87a18a'
            elif hllen == 1:
                event.background_color = '#10b326'
            elif hllen == 2:
                event.background_color = 'fff833'
            elif hllen == 3:
                event.background_color = '#ff2200'
            elif hllen == 4:
                event.background_color = '#5c0313'
            elif hllen == 5:
                event.background_color = '#2e0109'

        
        """ #s_counter = 0
        t_counter = 0
        tw_counter = 0
        tr_counter = 0
        if event.text == "split":
            self.sp_counter += 1
            if self.sp_counter == 1:
                event.background_color = '#10b326'
                
            elif self.sp_counter == 2:
                event.background_color = 'fff833'
                
            else:
                event.background_color = 'e43214'
            
        elif event.text == "10-5":
            self.te_counter += 1
            if self.te_counter == 1:
                event.background_color = '#10b326'
                
            elif self.te_counter == 2:
                event.background_color = 'fff833'
                
            else:
                event.background_color = 'e43214'

        elif event.text == "12-11":
            self.twe_counter += 1
            if self.twe_counter == 1:
                event.background_color = '#10b326'
                
            elif self.twe_counter == 2:
                event.background_color = 'fff833'
                
            else:
                event.background_color = 'e43214'

        else:
            self.tre_counter += 1
            if self.tre_counter == 1:
                event.background_color = '#10b326'
                
            elif self.tre_counter == 2:
                event.background_color = 'fff833'
                
            else:
                event.background_color = 'e43214' """
                




    
    def addshift_to_mustdo(self,event):
        #test = []
        #lunghezza = len(test)
        #if lunghezza > 1:
            #self.addshift.background_color == 'e43214'
        
        if event.text == "split":
            self.listof_mustdo.append("a " + event.text)
            #test.append("a")
            self.s_counter += 1
            
        if event.text == "10-5":
            self.listof_mustdo.append("b "+ event.text)
            self.t_counter += 1
            #test.append("a")
            
        if event.text == "3-f":
            self.listof_mustdo.append("d "+ event.text)
            self.tr_counter += 1
            
        if event.text == "12-11":
            self.listof_mustdo.append("c " + event.text)
            self.tw_counter += 1
        
        if event.text == "holiday":
            self.listof_mustdo.append("e " + event.text)
            self.hl_counter += 1
            


    def add_mustto_tolabel(self,evet):
        bob = self.listof_mustdo
        newLin = '\n'
        a= ""
        b= ""
        c= ""
        b= ""
        e= ""
        f= ""
        if len(bob) == 0:
            stry = ""
        elif len(bob) == 1:
            a= bob[0]
            stry = f"{a}"
        elif len(bob) == 2:
            a= bob[0]
            b= bob[1]
            stry = f"{a}{newLin}{b}"
        elif len(bob) == 3:
            a= bob[0]
            b= bob[1]
            c= bob[2]
            stry = f"{a}{newLin}{b}{newLin}{c}"
        elif len(bob) == 4:
            a= bob[0]
            b= bob[1]
            c= bob[2]
            d= bob[3]
            stry = f"{a}{newLin}{b}{newLin}{c}{newLin}{d}"
        elif len(bob) == 5:
            a= bob[0]
            b= bob[1]
            c= bob[2]
            d= bob[3]
            e= bob[4]
            stry = f"{a}{newLin}{b}{newLin}{c}{newLin}{d}{newLin}{e}"
        elif len(bob) == 6:
            a= bob[0]
            b= bob[1]
            c= bob[2]
            d= bob[3]
            e= bob[4]
            f= bob[5]  
            stry = f"{a}{newLin}{b}{newLin}{c}{newLin}{d}{newLin}{e}{newLin}{f}"
        x = stry
        #x = str(self.listof_mustdo)
        self.mustdolabel.text = x
        #newline = '\n'
        #str = fa{newline}Java{newline}Cpp"
        #print(str)
            

        


class Day(Widget):
    def __init__(self, name,**kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.m = TextInput(multiline = False)
        self.l = TextInput(multiline = False)
        self.b = TextInput(multiline = False)
        self.d = TextInput(multiline = False)

        self.mr =  Label(text = "4")
        self.lr =  Label(text = "6")
        self.br =  Label(text = "4")
        self.dr =  Label(text = "8")

        newLin = '\n'
        

        self.allsplit = 0 
        self.alltens = 0
        self.alltwelv = 0
        self.alltre = 0
        self.allhol = 0

        self.m_int = 0
        self.l_int = 0
        self.b_int = 0
        self.d_int = 0

        self.updated_number = Label(text = "", italic = True) # size_hint_y=None height=150

        self.max = 7

        self.split_max = 1
        self.ten_max = 3

        
        #self.label = Button(text = self.name,background_color = '#87a18a')
        #self.label.bind(on_press = self.turnDay_on_off)
        
        self.bt = Button(text = "update day", bold = True,background_color = '#87a18a')
        self.bt.bind(on_press = self.update)

        self.list_ofshift_assigned = []
        
        self.partimers_shift_list = []
        
        self.listof_staff_inday = []
    
        self.day_shift_label = Label(text = str(self.list_ofshift_assigned))

        self.dactive = False

    #def turnDay_on_off(self,event):
        
        #if self.dactive == False:
            #self.dactive = True
            #event.background_color = '#0e630f'
        #elif self.dactive == True:
            #self.dactive = False
            #event.background_color = '#87a18a'
        

    def update(self,event):
        event.background_color = '#0e630f'
        mt = self.m.text        # store text input value into local variable
        lt = self.l.text
        bt = self.b.text
        dt = self.d.text

        lenmt = len(mt)
        lenlt = len(lt)
        lenbt = len(bt)
        lendt = len(dt)

        fixed_m = self.mr.text    # store the value of the Label
        fixed_l = self.lr.text
        fixed_b = self.br.text
        fixed_d = self.dr.text


        if lenmt == 0:
            self.m_int = int(fixed_m)
        else:
            self.mr.text = mt
            self.m_int = int(mt)  
        
        if lenlt == 0:
            self.l_int = int(fixed_l)
        else:
            self.lr.text = lt
            self.l_int = int(lt) 
        
        if lenbt == 0:
            self.b_int = int(fixed_b)
        else:
            self.br.text = bt
            self.b_int = int(bt) 
        
        if lendt == 0:
            self.d_int = int(fixed_d)
        else:
            self.dr.text = dt
            self.d_int = int(dt) 


        #self.mr.text = mt        # set the label taxt == to text imput local variable
        #self.lr.text = lt
        #self.br.text = bt
        #self.dr.text = dt

        #new_mt = self.mr.text      # set a new local variable to be the same as the label text
        #new_lt = self.lr.text       #  so if the label does not get updated, the day.m.l.b.d will be the same as label
        #new_bt = self.br.text
        #new_dt = self.dr.text

        
        


class Rota(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.dayGrid  = GridLayout()
        self.dayGrid.cols = 10

        self.staffGrid  = GridLayout()
        self.staffGrid.cols = 9

        self.daynumbers = GridLayout()
        self.daynumbers.cols = 5

        self.partime = GridLayout()
        self.partime.cols = 8

        self.beforedaygrid = Label(text = "Update each day staff requirements", size_hint_y=None, height=40)
        self.beforestaffgrid = Label(text = "Assigned shift to each fulltime staff", size_hint_y=None, height=40)

        self.sat = Day("saturday")
        self.tue = Day("tuesday")
        self.wed = Day("wednesday")
        self.thu = Day("thursday")
        self.fri = Day("friday")

        self.all_days = [self.sat,self.tue,self.wed, self.thu, self.fri]

        self.fede = Staff("  Fede ")
        self.annie = Staff("  Annie ")
        self.krzy = Staff("  Krzy ")
        self.matt = Staff("  Matt ")
        self.steven = Staff("  Steven ")
        self.jenn = Staff("  Jenn ")
        self.jess = Staff("  Jess ")

        self.bob = Staff("Bob")
        self.james = Staff("James")
        self.paul = Staff("Paul")
        self.brian = Staff("Brian")
        self.beth = Staff("Beth")
        self.freya = Staff("Freya")
        self.celine = Staff("Celine")
        self.phoebe = Staff("Phoebe")
        self.brooke = Staff("Brooke")
        self.karolina = Staff("Karolina")
        self.lily = Staff("Lily")
        self.anastasia = Staff("Anastasia")
        self.nafisa = Staff("Nafisa")
        self.william = Staff("William")
        self.maddie = Staff("Maddie")

        self.split_shift = Button(text = "split ",background_color = '#8f9596')
        self.ten_shift = Button(text = "10-5 ",background_color = '#8f9596')
        self.fiv_shift = Button(text = "5-f ",background_color = '#8f9596' )
        self.twelv_shift = Button(text = "12-11 ",background_color = '#8f9596')
        self.tre_shift = Button(text = "3-f ",background_color = '#8f9596')
        self.off_shift = Button(text = "off ",background_color = '#8f9596')

        self.split_shift.bind(on_press = self.distribute_partime)
        self.ten_shift.bind(on_press = self.distribute_partime)
        self.twelv_shift.bind(on_press = self.distribute_partime)
        self.tre_shift.bind(on_press = self.distribute_partime)
        self.fiv_shift.bind(on_press = self.distribute_partime)
        self.off_shift.bind(on_press = self.distribute_partime)
        
        # days

        self.saturdayD = Button(text = "saturday")
        self.tuesdayD = Button(text = "tuesday")
        self.wednesdayD = Button(text = "wednesday")
        self.thursdayD = Button(text = "thursday")
        self.fridayD = Button(text = "friday")
        
        self.dayList = [self.saturdayD,self.tuesdayD,self.wednesdayD,self.thursdayD,self.fridayD]

        self.saturdayD.bind(on_press = self.switch_days_on_off)
        self.tuesdayD.bind(on_press = self.switch_days_on_off)
        self.wednesdayD.bind(on_press = self.switch_days_on_off)
        self.thursdayD.bind(on_press = self.switch_days_on_off)
        self.fridayD.bind(on_press = self.switch_days_on_off)

        # STAFF

        self.bobD = Button(text = "Bob")
        self.jamesD = Button(text = "James")
        self.paulD = Button(text = "Paul")
        self.brianD = Button(text = "Brian")
        self.bethD = Button(text = "Beth")
        self.freyaD = Button(text = "Freya")
        self.celineD = Button(text = "Celine")
        self.phoebeD = Button(text = "Phoebe")
        self.brookeD = Button(text = "Brooke")
        self.karolinaD = Button(text = "Karolina")
        self.lilyD = Button(text = "Lily")
        self.anastasiaD = Button(text = "Anastasia")
        self.nafisaD = Button(text = "Nafisa")
        self.williamD = Button(text = "William")
        self.maddieD = Button(text = "Maddie")

        self.all_Dpartime = [self.bobD,self.jamesD,self.paulD,self.brianD,self.bethD,self.freyaD,self.celineD,self.phoebeD,self.brookeD,self.karolinaD,self.lilyD,self.anastasiaD, self.nafisaD, self.williamD ,self.maddieD]
        
        self.bobD.bind(on_press = self.switch_staff_on_off)
        self.jamesD.bind(on_press = self.switch_staff_on_off)
        self.paulD.bind(on_press = self.switch_staff_on_off)
        self.brianD.bind(on_press = self.switch_staff_on_off)
        self.bethD.bind(on_press = self.switch_staff_on_off)
        self.freyaD.bind(on_press = self.switch_staff_on_off)
        self.celineD.bind(on_press = self.switch_staff_on_off)
        self.phoebeD.bind(on_press = self.switch_staff_on_off)
        self.brookeD.bind(on_press = self.switch_staff_on_off)
        self.karolinaD.bind(on_press = self.switch_staff_on_off)
        self.lilyD.bind(on_press = self.switch_staff_on_off)
        self.anastasiaD.bind(on_press = self.switch_staff_on_off)
        self.nafisaD.bind(on_press = self.switch_staff_on_off)
        self.williamD.bind(on_press = self.switch_staff_on_off)
        self.maddieD.bind(on_press = self.switch_staff_on_off)


        self.all_staff = [self.jenn,self.jess,self.fede,self.annie,self.krzy,self.matt,self.steven]
        self.all_partime = [self.bob,self.james,self.paul,self.brian,self.beth,self.freya,self.celine,self.phoebe,self.brooke,self.karolina,self.lily,self.anastasia, self.nafisa, self.william ,self.maddie]

        self.ninethwiget = Button(text = "add to day")

        #self.testlist = []
        #self.lenght_testlist = len(self.testlist)
        #self.testlist_label = Label(text = str(self.lenght_testlist))

        self.overall_mustdo_list = []

        self.sorted_mustdo = []

        self.newlin = '\n'

        self.display_label = Button(text = f"view {self.newlin}label",background_color = '#043240')
        self.display_label.bind(on_press = self.update_midjob_label)
        
        self.add_to_overallmustdo = Button(text = f"add to {self.newlin}averall")
        self.add_to_overallmustdo.bind(on_press = self.move_eachmustdo_into_overall)

        self.combine_finalise = Button(text = f"finalise {self.newlin}rota")
        self.combine_finalise.bind(on_press = self.combine)

        self.assigne_mustdo_to_day = Button(text = f"assign {self.newlin}mustdo")
        self.assigne_mustdo_to_day.bind(on_press = self.assign_mustdo_todays)

        self.exelButton = Button(text = "exel")
        self.exelButton.bind(on_press = self.create_doc)

        self.finalBut = Button(text = f"Finalise{self.newlin}Rota",background_color = '#043240')  #size_hint_y=None, height=50
        self.finalBut.bind(on_press = self.final)


        
        

        
        self.dayGrid.add_widget(self.saturdayD)
        self.dayGrid.add_widget(self.sat.m)
        self.dayGrid.add_widget(self.sat.l)
        self.dayGrid.add_widget(self.sat.b)
        self.dayGrid.add_widget(self.sat.d)
        self.dayGrid.add_widget(self.sat.bt)
        self.dayGrid.add_widget(self.sat.mr)
        self.dayGrid.add_widget(self.sat.lr)
        self.dayGrid.add_widget(self.sat.br)
        self.dayGrid.add_widget(self.sat.dr)

        self.dayGrid.add_widget(self.tuesdayD)
        self.dayGrid.add_widget(self.tue.m)
        self.dayGrid.add_widget(self.tue.l)
        self.dayGrid.add_widget(self.tue.b)
        self.dayGrid.add_widget(self.tue.d)
        self.dayGrid.add_widget(self.tue.bt)
        self.dayGrid.add_widget(self.tue.mr)
        self.dayGrid.add_widget(self.tue.lr)
        self.dayGrid.add_widget(self.tue.br)
        self.dayGrid.add_widget(self.tue.dr)

        self.dayGrid.add_widget(self.wednesdayD)
        self.dayGrid.add_widget(self.wed.m)
        self.dayGrid.add_widget(self.wed.l)
        self.dayGrid.add_widget(self.wed.b)
        self.dayGrid.add_widget(self.wed.d)
        self.dayGrid.add_widget(self.wed.bt)
        self.dayGrid.add_widget(self.wed.mr)
        self.dayGrid.add_widget(self.wed.lr)
        self.dayGrid.add_widget(self.wed.br)
        self.dayGrid.add_widget(self.wed.dr)

        self.dayGrid.add_widget(self.thursdayD)
        self.dayGrid.add_widget(self.thu.m)
        self.dayGrid.add_widget(self.thu.l)
        self.dayGrid.add_widget(self.thu.b)
        self.dayGrid.add_widget(self.thu.d)
        self.dayGrid.add_widget(self.thu.bt)
        self.dayGrid.add_widget(self.thu.mr)
        self.dayGrid.add_widget(self.thu.lr)
        self.dayGrid.add_widget(self.thu.br)
        self.dayGrid.add_widget(self.thu.dr)

        self.dayGrid.add_widget(self.fridayD)
        self.dayGrid.add_widget(self.fri.m)
        self.dayGrid.add_widget(self.fri.l)
        self.dayGrid.add_widget(self.fri.b)
        self.dayGrid.add_widget(self.fri.d)
        self.dayGrid.add_widget(self.fri.bt)
        self.dayGrid.add_widget(self.fri.mr)
        self.dayGrid.add_widget(self.fri.lr)
        self.dayGrid.add_widget(self.fri.br)
        self.dayGrid.add_widget(self.fri.dr)

        self.staffGrid.add_widget(self.fede.staflabel)
        self.staffGrid.add_widget(self.fede.hol)
        self.staffGrid.add_widget(self.fede.split)
        self.staffGrid.add_widget(self.fede.tenf)
        self.staffGrid.add_widget(self.fede.tre)
        self.staffGrid.add_widget(self.fede.twel)
        self.staffGrid.add_widget(self.fede.addshift)
        self.staffGrid.add_widget(self.fede.delete_butt)
        self.staffGrid.add_widget(self.fede.mustdolabel)
        

        self.staffGrid.add_widget(self.annie.staflabel)
        self.staffGrid.add_widget(self.annie.hol)
        self.staffGrid.add_widget(self.annie.split)
        self.staffGrid.add_widget(self.annie.tenf)
        self.staffGrid.add_widget(self.annie.tre)
        self.staffGrid.add_widget(self.annie.twel)
        self.staffGrid.add_widget(self.annie.addshift)
        self.staffGrid.add_widget(self.annie.delete_butt)
        self.staffGrid.add_widget(self.annie.mustdolabel)
       

        self.staffGrid.add_widget(self.krzy.staflabel)
        self.staffGrid.add_widget(self.krzy.hol)
        self.staffGrid.add_widget(self.krzy.split)
        self.staffGrid.add_widget(self.krzy.tenf)
        self.staffGrid.add_widget(self.krzy.tre)
        self.staffGrid.add_widget(self.krzy.twel)
        self.staffGrid.add_widget(self.krzy.addshift)
        self.staffGrid.add_widget(self.krzy.delete_butt)
        self.staffGrid.add_widget(self.krzy.mustdolabel)
        
        
        self.staffGrid.add_widget(self.matt.staflabel)
        self.staffGrid.add_widget(self.matt.hol)
        self.staffGrid.add_widget(self.matt.split)
        self.staffGrid.add_widget(self.matt.tenf)
        self.staffGrid.add_widget(self.matt.tre)
        self.staffGrid.add_widget(self.matt.twel)
        self.staffGrid.add_widget(self.matt.addshift)
        self.staffGrid.add_widget(self.matt.delete_butt)
        self.staffGrid.add_widget(self.matt.mustdolabel)
        

        self.staffGrid.add_widget(self.steven.staflabel)
        self.staffGrid.add_widget(self.steven.hol)
        self.staffGrid.add_widget(self.steven.split)
        self.staffGrid.add_widget(self.steven.tenf)
        self.staffGrid.add_widget(self.steven.tre)
        self.staffGrid.add_widget(self.steven.twel)
        self.staffGrid.add_widget(self.steven.addshift)
        self.staffGrid.add_widget(self.steven.delete_butt)
        self.staffGrid.add_widget(self.steven.mustdolabel)
        

        self.staffGrid.add_widget(self.jenn.staflabel)
        self.staffGrid.add_widget(self.jenn.hol)
        self.staffGrid.add_widget(self.jenn.split)
        self.staffGrid.add_widget(self.jenn.tenf)
        self.staffGrid.add_widget(self.jenn.tre)
        self.staffGrid.add_widget(self.jenn.twel)
        self.staffGrid.add_widget(self.jenn.addshift)
        self.staffGrid.add_widget(self.jenn.delete_butt)
        self.staffGrid.add_widget(self.jenn.mustdolabel)
        

        self.staffGrid.add_widget(self.jess.staflabel)
        self.staffGrid.add_widget(self.jess.hol)
        self.staffGrid.add_widget(self.jess.split)
        self.staffGrid.add_widget(self.jess.tenf)
        self.staffGrid.add_widget(self.jess.tre)
        self.staffGrid.add_widget(self.jess.twel)
        self.staffGrid.add_widget(self.jess.addshift)
        self.staffGrid.add_widget(self.jess.delete_butt)
        self.staffGrid.add_widget(self.jess.mustdolabel)

        self.daynumbers.add_widget(self.sat.updated_number)
        self.daynumbers.add_widget(self.tue.updated_number)
        self.daynumbers.add_widget(self.wed.updated_number)
        self.daynumbers.add_widget(self.thu.updated_number)
        self.daynumbers.add_widget(self.fri.updated_number)
        #self.daynumbers.add_widget(Label(text = ""))
        #self.daynumbers.add_widget(Label(text = ""))
        #self.daynumbers.add_widget(self.beforestaffgrid)
        #self.daynumbers.add_widget(Label(text = ""))
        #self.daynumbers.add_widget(Label(text = ""))

        self.partime.add_widget(self.bobD)
        self.partime.add_widget(self.jamesD)
        self.partime.add_widget(self.bethD)
        self.partime.add_widget(self.karolinaD)
        self.partime.add_widget(self.celineD)
        self.partime.add_widget(self.paulD)
        self.partime.add_widget(self.brianD)
        self.partime.add_widget(self.brookeD)
        self.partime.add_widget(self.freyaD)
        self.partime.add_widget(self.maddieD)
        self.partime.add_widget(self.phoebeD)
        self.partime.add_widget(self.lilyD)
        self.partime.add_widget(self.anastasiaD)
        self.partime.add_widget(self.nafisaD)
        self.partime.add_widget(self.williamD)
        self.partime.add_widget(self.display_label)
        self.partime.add_widget(self.split_shift)
        self.partime.add_widget(self.ten_shift)
        self.partime.add_widget(self.twelv_shift)
        self.partime.add_widget(self.tre_shift)
        self.partime.add_widget(self.fiv_shift)
        self.partime.add_widget(self.off_shift)
        self.partime.add_widget(Label(text = ""))
        self.partime.add_widget(self.finalBut)
        
        #self.add_widget(self.beforedaygrid)
        self.add_widget(self.dayGrid)
        self.add_widget(self.partime)
        #self.add_widget(self.daynumbers)
        self.add_widget(self.staffGrid)
        #self.add_widget(self.finalBut)
        self.add_widget(self.daynumbers)
        #self.add_widget(self.partime)
        #self.add_widget(self.daynumbers)
        
        #self.add_widget(self.add_to_overallmustdo)
        #self.add_widget(self.assigne_mustdo_to_day)
        #self.add_widget(self.combine_finalise)
        #self.add_widget(self.exelButton)
        #self.add_widget(self.finalBut)

    def switch_staff_on_off(self,event):
        buttony = event.text
        for staf in self.all_partime:
            if staf.name == buttony:
                staf.sactive = True
                
                
            else:
                staf.sactive = False
                
        for butt in self.all_Dpartime:
            for staf in self.all_partime:
                if staf.name == butt.text:
                    if staf.sactive == True:
                        butt.background_color = '#0e630f'
                    else:
                        butt.background_color = '#87a18a'
        

        
    
    def switch_days_on_off(self,event):
        buttonx = event.text
        for day in self.all_days:
            if day.name == buttonx:
                day.dactive = True
                
                
            else:
                day.dactive = False
                
        for but in self.dayList:
            for day in self.all_days:
                if day.name == but.text:
                    if day.dactive == True:
                        but.background_color = '#0e630f'
                    else:
                        but.background_color = '#87a18a'
        

        




    def distribute_partime(self,event):
        x = event.text
        for staf in self.all_partime:
            if staf.sactive == True:
                for day in self.all_days:
                    if day.dactive == True:
                        if day.name == "saturday":
                            staf.end_list[2] = event.text
                            if x == "split ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.d_int -= 1
                            elif x == "10-5 ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.b_int -= 1
                            elif x == "12-11 ":
                                day.l_int -= 1
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "3-f ":
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "5-f ":
                                day.d_int -= 1        
                        elif day.name == "tuesday":
                            staf.end_list[3] = event.text
                            if x == "split ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.d_int -= 1
                            elif x == "10-5 ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.b_int -= 1
                            elif x == "12-11 ":
                                day.l_int -= 1
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "3-f ":
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "5-f ":
                                day.d_int -= 1 
                        elif day.name == "wednesday":
                            staf.end_list[4] = event.text
                            if x == "split ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.d_int -= 1
                            elif x == "10-5 ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.b_int -= 1
                            elif x == "12-11 ":
                                day.l_int -= 1
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "3-f ":
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "5-f ":
                                day.d_int -= 1 
                        elif day.name == "thursday":
                            staf.end_list[5] = event.text
                            if x == "split ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.d_int -= 1
                            elif x == "10-5 ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.b_int -= 1
                            elif x == "12-11 ":
                                day.l_int -= 1
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "3-f ":
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "5-f ":
                                day.d_int -= 1 
                        elif day.name == "friday":
                            staf.end_list[6] = event.text
                            if x == "split ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.d_int -= 1
                            elif x == "10-5 ":
                                day.m_int -= 1
                                day.l_int -= 1
                                day.b_int -= 1
                            elif x == "12-11 ":
                                day.l_int -= 1
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "3-f ":
                                day.b_int -= 1
                                day.d_int -= 1
                            elif x == "5-f ":
                                day.d_int -= 1 

        

        self.update_midjob_label(event)

        
       
        
        
        

    def update_midjob_label(self,event):
        for day in self.all_days:
            day.updated_number.text = f"{self.newlin}{day.name}{self.newlin}{self.newlin}Momrnig: {day.m_int}{self.newlin}Lunch: {day.l_int}{self.newlin}Back: {day.b_int}{self.newlin}Dinner: {day.d_int}"

    def final(self,event):
        self.move_eachmustdo_into_overall(event)
        self.assign_mustdo_todays(event)
        self.combine(event)
        self.create_doc(event)
        self.update_midjob_label(event)
    
    def create_doc(self,event):
        MorningN = ["Morning"]
        LunchN = ["Lunch"] 
        BackN = ["Back"] 
        DinnerN = ["Dinner"]  
        header = ["names"]
        sorted_steven = sorted(self.steven.end_list_shift)
        sorted_fede = sorted(self.fede.end_list_shift)
        sorted_matt = sorted(self.matt.end_list_shift)
        sorted_annie = sorted(self.annie.end_list_shift)
        sorted_krzy = sorted(self.krzy.end_list_shift)
        sorted_jenn = sorted(self.jenn.end_list_shift)
        sorted_jess = sorted(self.jess.end_list_shift)
        
        sorted_bob = self.bob.end_list
        sorted_james = self.james.end_list
        sorted_paul = self.paul.end_list
        sorted_brian = self.brian.end_list
        sorted_beth = self.beth.end_list
        sorted_freya = self.freya.end_list
        sorted_celine = self.celine.end_list
        sorted_phoebe = self.phoebe.end_list
        sorted_brooke = self.brooke.end_list
        sorted_karolina = self.karolina.end_list 
        sorted_lily = self.lily.end_list
        sorted_anastasia = self.anastasia.end_list 
        sorted_nafisa = self.nafisa.end_list
        sorted_william = self.william.end_list
        sorted_maddie = self.maddie.end_list    
        
        #allro= [ro1,ro2,ro3,ro4,ro5,ro6,ro7]

        edited_steven = []
        edited_fede = []
        edited_matt = []
        edited_annie = []
        edited_krzy = []
        edited_jenn = []
        edited_jess = []
        
        
        
        for n in sorted_steven:
            edited_steven.append(str(n[2:]))
        for n in sorted_fede:
            edited_fede.append(str(n[2:]))
        for n in sorted_matt:
            edited_matt.append(str(n[2:]))
        for n in sorted_annie:
            edited_annie.append(str(n[2:]))
        for n in sorted_krzy:
            edited_krzy.append(str(n[2:]))
        for n in sorted_jenn:
            edited_jenn.append(str(n[2:]))
        for n in sorted_jess:
            edited_jess.append(str(n[2:]))
        
        



        #data = [ro1,ro2,ro3,ro4,ro5,ro6,ro7]
        for day in self.all_days:
            header.append(" " + day.name)
        
        for day in self.all_days:
            MorningN.append(" " + str(day.m_int))
        for day in self.all_days:
            LunchN.append(" " + str(day.l_int))
        for day in self.all_days:
            BackN.append(" " + str(day.b_int))
        for day in self.all_days:
            DinnerN.append(" " + str(day.d_int))
        
        
        with open("test.csv",'w', newline='')as f:
            writer = csv.writer(f)
            
            
            writer.writerow(header)
            writer.writerow(edited_steven)
            writer.writerow(edited_matt)
            writer.writerow(edited_fede)
            writer.writerow(edited_annie)
            writer.writerow(edited_krzy)
            writer.writerow(edited_jenn)
            writer.writerow(edited_jess)
            
            writer.writerow(sorted_bob)
            writer.writerow(sorted_james)
            writer.writerow(sorted_paul)
            writer.writerow(sorted_brian)
            writer.writerow(sorted_beth)
            writer.writerow(sorted_freya)
            writer.writerow(sorted_celine)
            writer.writerow(sorted_phoebe)
            writer.writerow(sorted_brooke)
            writer.writerow(sorted_karolina)
            writer.writerow(sorted_lily)
            writer.writerow(sorted_anastasia)
            writer.writerow(sorted_nafisa)
            writer.writerow(sorted_william)
            writer.writerow(sorted_maddie)
            # bob james paul brian beth freya celine phoebe brooke karolina lily ana nafisa william maddie
            
            writer.writerow(MorningN)
            writer.writerow(LunchN)
            writer.writerow(BackN)
            writer.writerow(DinnerN)

        
    def combine(self,event):
        

        sat = []
        tue = []
        wed = []
        thu = []
        fri = []
        
        for day in self.all_days:
            if day.name == "saturday":
                for shift in day.list_ofshift_assigned:
                    sat.append(shift)
        for day in self.all_days:
            if day.name == "tuesday":
                for shift in day.list_ofshift_assigned:
                    tue.append(shift)
        for day in self.all_days:
            if day.name == "wednesday":
                for shift in day.list_ofshift_assigned:
                    wed.append(shift)
        for day in self.all_days:
            if day.name == "thursday":
                for shift in day.list_ofshift_assigned:
                    thu.append(shift)
        for day in self.all_days:
            if day.name == "friday":
                for shift in day.list_ofshift_assigned:
                    fri.append(shift)

        
        
        for staf in self.all_staff:
            for shift in staf.listof_mustdo:
                if shift in sat:
                    if staf.sat_is_empty:
                        if shift == "a split":
                            if staf.s_counter > 0:
                                staf.end_list_shift.append("a." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.s_counter -= 1
                                staf.sat_is_empty = False
                                sat.remove(shift)
                        if shift == "b 10-5":
                            if staf.t_counter > 0:
                                staf.end_list_shift.append("a." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.t_counter -= 1
                                staf.sat_is_empty = False
                                sat.remove(shift)
                        if shift == "c 12-11":
                            if staf.tw_counter > 0:
                                staf.end_list_shift.append("a." + (str(shift[2:])) + " ")
                                #staf.end_list_shift.append(shift)
                                staf.tw_counter -= 1
                                staf.sat_is_empty = False
                                sat.remove(shift)
                        if shift == "d 3-f":
                            if staf.tr_counter > 0:
                                staf.end_list_shift.append("a." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.tr_counter -= 1
                                staf.sat_is_empty = False
                                sat.remove(shift)
                        if shift == "e holiday":
                            if staf.hl_counter > 0:
                                staf.end_list_shift.append("a." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.hl_counter -= 1
                                staf.sat_is_empty = False
                                sat.remove(shift)
                
                
                if shift in tue:
                    if staf.tue_is_empty:
                        if shift == "a split":
                            if staf.s_counter > 0:
                                staf.end_list_shift.append("b." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.s_counter -= 1
                                staf.tue_is_empty = False
                                tue.remove(shift)
                        if shift == "b 10-5":
                            if staf.t_counter > 0:
                                staf.end_list_shift.append("b." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.t_counter -= 1
                                staf.tue_is_empty = False
                                tue.remove(shift)
                        if shift == "c 12-11":
                            if staf.tw_counter > 0:
                                staf.end_list_shift.append("b."+ (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.tw_counter -= 1
                                staf.tue_is_empty = False
                                tue.remove(shift)
                        if shift == "d 3-f":
                            if staf.tr_counter > 0:
                                staf.end_list_shift.append("b."+ (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.tr_counter -= 1
                                staf.tue_is_empty = False
                                tue.remove(shift)
                        if shift == "e holiday":
                            if staf.hl_counter > 0:
                                staf.end_list_shift.append("b." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.hl_counter -= 1
                                staf.tue_is_empty = False
                                tue.remove(shift)
                
                
                if shift in wed:
                    if staf.wed_is_empty:
                        if shift == "a split":
                            if staf.s_counter > 0:
                                staf.end_list_shift.append("c." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.s_counter -= 1
                                staf.wed_is_empty = False
                                wed.remove(shift)
                        if shift == "b 10-5":
                            if staf.t_counter > 0:
                                staf.end_list_shift.append("c."+ (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.t_counter -= 1
                                staf.wed_is_empty = False
                                wed.remove(shift)
                        if shift == "c 12-11":
                            if staf.tw_counter > 0:
                                staf.end_list_shift.append("c."+ (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.tw_counter -= 1
                                staf.wed_is_empty = False
                                wed.remove(shift)
                        if shift == "d 3-f":
                            if staf.tr_counter > 0:
                                staf.end_list_shift.append("c." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.tr_counter -= 1
                                staf.wed_is_empty = False
                                wed.remove(shift)
                        if shift == "e holiday":
                            if staf.hl_counter > 0:
                                staf.end_list_shift.append("c." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.hl_counter -= 1
                                staf.wed_is_empty = False
                                wed.remove(shift)
                
                
                if shift in thu:
                    if staf.thu_is_empty:
                        if shift == "a split":
                            if staf.s_counter > 0:
                                staf.end_list_shift.append("d." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.s_counter -= 1
                                staf.thu_is_empty = False
                                thu.remove(shift)
                        if shift == "b 10-5":
                            if staf.t_counter > 0:
                                staf.end_list_shift.append("d." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.t_counter -= 1
                                staf.thu_is_empty = False
                                thu.remove(shift)
                        if shift == "c 12-11":
                            if staf.tw_counter > 0:
                                staf.end_list_shift.append("d."+  (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.tw_counter -= 1
                                staf.thu_is_empty = False
                                thu.remove(shift)
                        if shift == "d 3-f":
                            if staf.tr_counter > 0:
                                staf.end_list_shift.append("d."+ (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.tr_counter -= 1
                                staf.thu_is_empty = False
                                thu.remove(shift)
                        if shift == "e holiday":
                            if staf.hl_counter > 0:
                                staf.end_list_shift.append("d." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.hl_counter -= 1
                                staf.thu_is_empty = False
                                thu.remove(shift)
                
                
                if shift in fri:
                    if staf.fri_is_empty:
                        if shift == "a split":
                            if staf.s_counter > 0:
                                staf.end_list_shift.append("e." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.s_counter -= 1
                                staf.fri_is_empty = False
                                fri.remove(shift)
                        if shift == "b 10-5":
                            if staf.t_counter > 0:
                                staf.end_list_shift.append("e." +  (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.t_counter -= 1
                                staf.fri_is_empty = False
                                fri.remove(shift)
                        if shift == "c 12-11":
                            if staf.tw_counter > 0:
                                staf.end_list_shift.append("e." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.tw_counter -= 1
                                staf.fri_is_empty = False
                                fri.remove(shift)
                        if shift == "d 3-f":
                            if staf.tr_counter > 0:
                                staf.end_list_shift.append("e." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.tr_counter -= 1
                                staf.fri_is_empty = False
                                fri.remove(shift)
                        if shift == "e holiday":
                            if staf.hl_counter > 0:
                                staf.end_list_shift.append("e." + (str(shift[2:]))+ " ")
                                #staf.end_list_shift.append(shift)
                                staf.hl_counter -= 1
                                staf.fri_is_empty = False
                                fri.remove(shift)



        

        for staff in self.all_staff:
            print(staff.name)
            #print(staff.listof_mustdo)
            #print(staff.end_list)
            print(staff.end_list_shift)    
        print(sat)
        print(tue)
        print(wed)
        print(thu)
        print(fri)

        
    def move_eachmustdo_into_overall(self,event):
        for staf in self.all_staff:
            for shift in staf.listof_mustdo:
                self.overall_mustdo_list.append(shift)

        #print(self.overall_mustdo_list)
        self.sorted_mustdo = sorted(self.overall_mustdo_list)
        print(self.sorted_mustdo)

    def assign_mustdo_todays(self,event):
        all_split = []
        all_ten = []
        all_tre = []
        all_twe = []
        all_hol = []

        for shift in self.overall_mustdo_list:
            if shift == "a split":
                all_split.append("1")
            elif shift == "b 10-5":
                all_ten.append("b")
            elif shift == "c 12-11":
                all_twe.append("c")
            elif shift == "d 3-f":
                all_tre.append("d")
            elif shift == "e holiday":
                all_hol.append("h")

        n_split = len(all_split)
        n_ten = len(all_ten)
        n_twe = len(all_twe)
        n_tre = len(all_tre)
        n_hol = len(all_hol)

        print(n_split)
        print(n_ten)
        print(n_twe)
        print(n_tre)
        print(n_hol)

        split_counter = 0
        ten_counter = 0
        twe_counter = 0
        tre_counter = 0
        hol_counter = 0

        #for day in self.all_days:
            #print(day.name)
            #print(day.m_int)
            #print(day.l_int)

        #print(n_split)
        #print(n_ten)
        #print(n_twe)
        #print(n_tre)
        #print(self.overall_mustdo_list)
        
        for day in self.all_days:
            for shift in self.sorted_mustdo:
            #for day in self.all_days:
                if day.max > 0: 
                    if shift == "a split":
                        if day.split_max > 0: 
                            if split_counter < n_split: 

                                if day.m_int > 0:
                                    if day.l_int > 0:
                                        day.list_ofshift_assigned.append(shift)
                                        day.allsplit += 1 
                                        day.split_max -= 1
                                        #print("split" + split_counter)
                                        split_counter += 1
                                        day.max -=1
                                        day.m_int -= 1
                                        day.l_int -= 1
                                        day.d_int -= 1
                    elif shift == "b 10-5":
                        if day.ten_max > 0:
                            if ten_counter < n_ten:
                                if day.m_int > 0:
                                    if day.l_int > 0:
                                        day.list_ofshift_assigned.append(shift)
                                        day.alltens += 1
                                        day.ten_max -= 1
                                        ten_counter += 1
                                        day.max -=1
                                        day.m_int -= 1
                                        day.l_int -= 1
                                        day.b_int -= 1 
                    elif shift == "d 3-f":
                        if tre_counter < n_tre:
                            day.list_ofshift_assigned.append(shift)
                            day.alltre += 1
                            tre_counter += 1
                            day.max -=1
                            day.b_int -= 1
                            day.d_int -= 1
                    elif shift == "c 12-11":
                        if twe_counter < n_twe:
                            if day.l_int > 0:
                                day.list_ofshift_assigned.append(shift)
                                day.alltwelv += 1
                                twe_counter += 1
                                day.max -=1
                                day.l_int -= 1
                                day.b_int -= 1
                                day.d_int -= 1
                    elif shift == "e holiday":
                        if hol_counter < n_hol:
                            #if day.l_int > 0:
                            day.list_ofshift_assigned.append(shift)
                            day.allhol += 1
                            hol_counter += 1
                            day.max -=1
                                #day.l_int -= 1
                                #day.b_int -= 1
                                #day.d_int -= 1
        
        #for day in self.all_days:


        for day in self.all_days:
            print(day.name)
            print("m " + str(day.m_int))
            print("l " + str(day.l_int))
            #print(day.l_int)
            print(day.list_ofshift_assigned)
            #print(day.allsplit)
            #print(day.alltens)
            #print(day.alltwelv)
            #print(day.alltre)
            print("------------")
    





    
class Main(App):
    def build(self):
        return Rota()

if __name__ == "__main__":
    Main().run()