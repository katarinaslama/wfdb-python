import numpy as np
from wfdb import readsignal

# NB: write np.array to CSV with:
# sig[:,1].tofile('test01_00s_channel1.csv',sep=',',format='%s')

#class test_read_format_16(): 

    #def setUp(self):
        # load the sample binary file
        #self.sig, self.fields = readsignal.rdsamp('sampledata/test01_00s', physical=0) 

    #def test_channel1(self):
        # load the expected results
        #channel1 = np.genfromtxt('tests/targetoutputdata/test01_00s_channel1.csv', delimiter=',')
        #assert np.array_equal(self.sig[:,0],channel1)

    #def test_channel2(self):
        # load the expected results
        #channel2 = np.genfromtxt('tests/targetoutputdata/test01_00s_channel2.csv', delimiter=',')
        #assert np.array_equal(self.sig[:,1],channel2)

    #def test_channel3(self):
        # load the expected results
        #channel3 = np.genfromtxt('tests/targetoutputdata/test01_00s_channel3.csv', delimiter=',')
        #assert np.array_equal(self.sig[:,2],channel3)
    
    #def test_channel4(self):
        # load the expected results
        #channel4 = np.genfromtxt('tests/targetoutputdata/test01_00s_channel4.csv', delimiter=',')
        #assert np.array_equal(self.sig[:,3],channel4)

        
class test_rdsamp():
        
    # Test 1 - Format 212/Entire signal/Physical 
    # Target file created with: rdsamp -r sampledata/100 -P | cut -f 2- > target1      
    def test_1(self):
        sig1, fields1=readsignal.rdsamp('sampledata/100')
        targetsig1=np.genfromtxt('tests/targetoutputdata/target1')
        assert np.array_equal(sig1, targetsig1)
        
    # Test 2 - Format 212/Selected Duration/Selected Channel/Digital
    # Target file created with: rdsamp -r sampledata/100 -f 1 -t 30 -s 1 | cut -f 2- > target2
    def test_2(self):
        sig2, fields2=readsignal.rdsamp('sampledata/100', sampfrom=360, sampto=10800, channels=[1], physical=0) 
        targetsig2=np.genfromtxt('tests/targetoutputdata/target2')
        assert np.array_equal(sig2, targetsig2)
    
    # Test 3 - Format 16/Entire signal/Digital
    # Target file created with: rdsamp -r sampledata/test01_00s | cut -f 2- > target3
    def test_3(self):
        sig3, fields3=readsignal.rdsamp('sampledata/test01_00s', physical=0)
        targetsig3=np.genfromtxt('tests/targetoutputdata/target3')
        assert np.array_equal(sig3, targetsig3)
        
    # Test 4 - Format 16 with byte offset/Selected Duration/Selected Channels/Physical
    # Target file created with: rdsamp -r sampledata/a103l -f 50 -t 160 -s 2 0 -P | cut -f 2- > target4
    def test_4(self):
        sig4, fields4=readsignal.rdsamp('sampledata/a103l', sampfrom=12500, sampto=40000, channels=[2, 0])
        targetsig4=np.genfromtxt('tests/targetoutputdata/target4')
        assert np.array_equal(sig4, targetsig4) 
    
    # Test 5 - Format 16 with byte offset/Selected Duration/Selected Channels/Digital
    # Target file created with: rdsamp -r sampledata/a103l -f 80 -s 0 1 | cut -f 2- > target5
    def test_5(self):
        sig5, fields5=readsignal.rdsamp('sampledata/a103l', sampfrom=20000, physical=0, channels=[0, 1])
        targetsig5=np.genfromtxt('tests/targetoutputdata/target5')
        assert np.array_equal(sig5, targetsig5) 
    
    # Test 6 - Format 80/Selected Duration/Selected Channels/Physical
    # Target file created with: rdsamp -r sampledata/3000003_0003 -f 1 -t 8 -s 1 -P | cut -f 2- > target6
    def test_6(self):
        sig6, fields6=readsignal.rdsamp('sampledata/3000003_0003', sampfrom=125, sampto=1000, channels=[1])
        targetsig6=np.genfromtxt('tests/targetoutputdata/target6')
        assert np.array_equal(sig6, targetsig6) 
    
    # Test 7 - Multi-dat/Entire signal/Digital
    # Target file created with: rdsamp -r sampledata/s0010_re | cut -f 2- > target7
    def test_7(self):
        sig7, fields7=readsignal.rdsamp('sampledata/s0010_re', physical=0)
        targetsig7=np.genfromtxt('tests/targetoutputdata/target7')
        assert np.array_equal(sig7, targetsig7) 
    
    # Test 8 - Multi-dat/Selected Duration/Selected Channels/Physical
    # Target file created with: rdsamp -r sampledata/s0010_re -f 5 -t 38 -P -s 13 0 4 8 3 | cut -f 2- > target8
    def test_8(self):
        sig8, fields8=readsignal.rdsamp('sampledata/s0010_re', sampfrom=5000, sampto=38000, channels=[13, 0, 4, 8, 3])
        targetsig8=np.genfromtxt('tests/targetoutputdata/target8')
        assert np.array_equal(sig8, targetsig8) 
        