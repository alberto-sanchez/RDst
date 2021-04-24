import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    comEnergy = cms.double(13000.0),
    ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table            = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2014_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt_2014.pdl'),
            list_forced_decays     = cms.vstring(
                'myB+',
                'myB-',
                'myB_c+',
                'myB_c-',
                'myanti-B0',
                'myB0',
                'myanti-B_s0',
                'myB_s0'
            ),        
            operates_on_particles = cms.vint32(),
            convertPythiaCodes = cms.untracked.bool(False),
            user_decay_embedded= cms.vstring(
"""
Alias      myanti-B0      anti-B0
Alias      myB0           B0
Alias      myB-           B-
Alias      myB+           B+
Alias      myanti-B_s0    anti-B_s0
Alias      myB_s0         B_s0
Alias      myD*+          D*+
Alias      myD*-          D*-
Alias      myD0           D0
Alias      myanti-D0      anti-D0
Alias      myD_1+         D_1+
Alias      myD_1-         D_1-
Alias      myD_10         D_10
Alias      myanti-D_10    anti-D_10
Alias      myD'_1+        D'_1+
Alias      myD'_1-        D'_1-
Alias      myD'_10        D'_10
Alias      myanti-D'_10   anti-D'_10
Alias      myD_2*+        D_2*+
Alias      myD_2*-        D_2*-
Alias      myD_2*0        D_2*0
Alias      myanti-D_2*0   anti-D_2*0
Alias      myD'_s1+       D'_s1+
Alias      myD'_s1-       D'_s1-
Alias      myD_s2*+       D_s2*+
Alias      myD_s2*-       D_s2*-
Alias      myD(2S)0       D(2S)0
Alias      myanti-D(2S)0  anti-D(2S)0
Alias      myD(2S)+       D(2S)+
Alias      myD(2S)-       D(2S)-
Alias      myD*(2S)0      D*(2S)0
Alias      myanti-D*(2S)0 anti-D*(2S)0
Alias      myD*(2S)+      D*(2S)+
Alias      myD*(2S)-      D*(2S)-
Alias      myB_c-         B_c-
Alias      myB_c+         B_c+
ChargeConj myanti-B0      myB0
ChargeConj myB-           myB+
ChargeConj myanti-B_s0    myB_s0
ChargeConj myD*+          myD*-
ChargeConj myD0           myanti-D0
ChargeConj myD_1+         myD_1-
ChargeConj myD_10         myanti-D_10
ChargeConj myD'_1+        myD'_1-
ChargeConj myD'_10        myanti-D'_10
ChargeConj myD_2*+        myD_2*-
ChargeConj myD_2*0        myanti-D_2*0
ChargeConj myD'_s1+       myD'_s1-
ChargeConj myD_s2*+       myD_s2*-
ChargeConj myD(2S)0       myanti-D(2S)0
ChargeConj myD(2S)+       myD(2S)-
ChargeConj myD*(2S)0      myanti-D*(2S)0
ChargeConj myD*(2S)+      myD*(2S)-
ChargeConj myB_c-         myB_c+

Decay myanti-B0
0.0493   myD*+    mu-       anti-nu_mu         PHOTOS  HQET2 1.207 0.920 1.406 0.853; #[Reconstructed PDG2011]
0.0042   myD_1+   mu-       anti-nu_mu         PHOTOS  ISGW2;
0.0046   myD'_1+  mu-       anti-nu_mu         PHOTOS  ISGW2;
0.0033   myD_2*+  mu-       anti-nu_mu         PHOTOS  ISGW2;
0.00045  myD*+    pi0       mu-  anti-nu_mu    PHOTOS  GOITY_ROBERTS;
0.0150   myD*+    tau-      anti-nu_tau                ISGW2; #[Reconstructed PDG2011]
0.0013   myD_1+   tau-      anti-nu_tau                ISGW2;
0.0020   myD'_1+  tau-      anti-nu_tau                ISGW2;
0.0020   myD_2*+  tau-      anti-nu_tau                ISGW2;
0.000000 myD(2S)+  mu-      anti-nu_mu         PHOTOS  ISGW2;
0.000000 myD*(2S)+ mu-      anti-nu_mu         PHOTOS  ISGW2;
0.000000 myD(2S)+  tau-     anti-nu_tau                ISGW2;
0.000000 myD*(2S)+ tau-     anti-nu_tau                ISGW2;
0.000305 myD*+    D-                                   SVS;
0.000610 myD*-    D+                                   SVS; #[Reconstructed PDG2011]
0.000820 myD*+    D*-                                  SVV_HELAMP 0.47 0.0 0.96 0.0 0.56 0.0; #[Reconstructed PDG2011]
0.008000 myD*+    D_s-                                 SVS; #[Reconstructed PDG2011]
0.017700 myD*+    D_s*-                                SVV_HELAMP 0.4904 0.0 0.7204 0.0 0.4904 0.0; #[Reconstructed PDG2011]
0.0006   myD'_1+  D_s-                                 SVS;
0.0012   myD'_1+  D_s*-                                SVV_HELAMP 0.48 0.0 0.734 0.0 0.48 0.0;
0.0012   myD_1+   D_s-                                 SVS;
0.0024   myD_1+   D_s*-                                SVV_HELAMP 0.48 0.0 0.734 0.0 0.48 0.0;
0.0042   myD_2*+  D_s-                                 STS;
0.0040   myD_2*+  D_s*-                                PHSP;
0.003100 myD*+    anti-D0   K-                         PHSP; #[Reconstructed PDG2011]
0.011800 myD*+    anti-D*0  K-                         PHSP; #[Reconstructed PDG2011]
0.0018   myD*+    D-        anti-K0                    PHSP;
0.0047   D+       myD*-     anti-K0                    PHSP;
0.007800 myD*+    D*-       anti-K0                    PHSP; #[Reconstructed PDG2011]
0.0025   myD*+    anti-D0   K*-                        PHSP;
0.0050   myD*+    anti-D*0  K*-                        PHSP;
0.0025   myD*+    D-        anti-K*0                   PHSP;
0.0025   D+       myD*-     anti-K*0                   PHSP;
0.0050   myD*+    D*-       anti-K*0                   PHSP;
0.0015   myD*+    D_s0*-                               SVS;
0.00930  myD*+    D_s1-                                SVV_HELAMP 0.4904 0. 0.7204 0. 0.4904 0.; #[Reconstructed PDG2011]
0.00083  D'_s1-   myD*+                                PHSP;
Enddecay
CDecay myB0

Decay myB-
0.0045   myD_10   mu-  anti-nu_mu        PHOTOS   ISGW2;
0.0040   myD'_10  mu-  anti-nu_mu        PHOTOS   ISGW2;
0.0033   myD_2*0  mu-  anti-nu_mu        PHOTOS   ISGW2;
0.006100 myD*+    pi-  mu- anti-nu_mu    PHOTOS   GOITY_ROBERTS;
0.000000 myD(2S)0  mu-  anti-nu_mu       PHOTOS   ISGW2;
0.000000 myD*(2S)0 mu-  anti-nu_mu       PHOTOS   ISGW2;
0.000000 myD(2S)0  tau- anti-nu_tau               ISGW2;
0.000000 myD*(2S)0 tau- anti-nu_tau               ISGW2;
0.0013   myD_10   tau- anti-nu_tau                ISGW2;
0.0020   myD'_10  tau- anti-nu_tau                ISGW2;
0.0020   myD_2*0  tau- anti-nu_tau                ISGW2;
0.0006   myD'_10  D_s-                   SVS;
0.0012   myD'_10  D_s*-                  SVV_HELAMP 0.48 0.0 0.734 0.0 0.48 0.0;
0.0012   myD_10   D_s-                   SVS;
0.0024   myD_10   D_s*-                  SVV_HELAMP 0.48 0.0 0.734 0.0 0.48 0.0;
0.0042   myD_2*0  D_s-                   STS;
0.0040   myD_2*0  D_s*-                  PHSP;
0.007800 D*0      myD*-     anti-K0      PHSP; #[Reconstructed PDG2011]
0.0005   myD*-    D+        K-           PHSP;
0.001500 D-       myD*+     K-           PHSP; #[Reconstructed PDG2011]
0.0015   myD*-    D*+       K-           PHSP;
0.0025   D0       myD*-     anti-K*0     PHSP;
0.0050   D*0      myD*-     anti-K*0     PHSP;
0.0005   myD*-    D+        K*-          PHSP;
0.0005   D-       myD*+     K*-          PHSP;
0.0010   myD*-    D*+       K*-          PHSP;
0.000390 myD*-    D0                     SVS; #[Reconstructed PDG2011]
0.00081  D*0      myD*-                  SVV_HELAMP 0.47 0.0 0.96 0.0 0.56 0.0; #[Reconstructed PDG2011]
0.00045  D0       myD'_s1-               PHSP;
0.00094  D*0      myD'_s1-               PHSP;
Enddecay
CDecay myB+

Decay myanti-B_s0
0.0070    myD'_s1+   mu-     anti-nu_mu  PHOTOS  ISGW2;
0.0070    myD_s2*+   mu-     anti-nu_mu  PHOTOS  ISGW2;
0.0028    myD'_s1+   tau-    anti-nu_tau         ISGW2;
0.0028    myD_s2*+   tau-    anti-nu_tau         ISGW2;
0.0150    D_s*+      myD*-   anti-K0     PHSP;
0.0050    D_s+       myD*-   anti-K0     PHSP;
0.0030    D_s*+      myD*-   anti-K*0    PHSP;
0.0025    D_s+       myD*-   anti-K*0    PHSP;
0.0017    myD*+      D_s-                SVS;
0.0017    D_s*-      myD*+               SVV_HELAMP  1.0 0.0 1.0 0.0 1.0 0.0;
0.0007    myD*-      D+      K0          PHSP;
0.0007    myD*-      D0      K+          PHSP;
0.0003    myD*-      D+      pi0   K0    PHSP;
0.0007    myD*-      D0      pi+   K0    PHSP;
0.0003    myD*-      D+      pi-   K+    PHSP;
0.0007    myD*-      D0      pi0   K+    PHSP;
Enddecay
CDecay myB_s0

Decay myD*+
1.000  myD0  pi+           VSS;
Enddecay
CDecay myD*-

Decay myD0
1.000  K-  pi+              PHSP;
Enddecay
CDecay myanti-D0

Decay myD_1+
0.3333 myD*+ pi0                        VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
0.6667 D*0 pi+                          VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
Enddecay
CDecay myD_1-

Decay myD_10
0.3333    D*0 pi0                          VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
0.6667    myD*+ pi-                        VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
Enddecay
CDecay myanti-D_10

Decay myD'_1+
0.3333    myD*+ pi0                        VVS_PWAVE  1.0 0.0 0.0 0.0 0.0 0.0;
0.6667    D*0 pi+                          VVS_PWAVE  1.0 0.0 0.0 0.0 0.0 0.0;
Enddecay
CDecay myD'_1-

Decay myD'_10
0.6667    myD*+ pi-                        VVS_PWAVE  1.0 0.0 0.0 0.0 0.0 0.0;
0.3333    D*0 pi0                          VVS_PWAVE  1.0 0.0 0.0 0.0 0.0 0.0;
Enddecay
CDecay myanti-D'_10

Decay myD_2*+
0.1030    myD*+ pi0                        TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
0.2090    D*0 pi+                          TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
0.2290    D+  pi0                          TSS;
0.4590    D0  pi+                          TSS;
Enddecay
CDecay myD_2*-

Decay myD_2*0
0.2090    myD*+ pi-                        TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
0.1030    D*0 pi0                          TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
0.2290    D0  pi0                          TSS;
0.4590    D+  pi-                          TSS;
Enddecay
CDecay myanti-D_2*0

Decay myD'_s1+
0.5000   myD*+ K0                            VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
0.5000   D*0 K+                              VVS_PWAVE  0.0 0.0 0.0 0.0 1.0 0.0;
0.0000   gamma D_s*+                         PHSP;
0.0000   gamma D_s+                          PHSP;
Enddecay
CDecay myD'_s1-

Decay myD_s2*+
0.0500    myD*+ K0                         TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
0.0500    D*0 K+                           TVS_PWAVE  0.0 0.0 1.0 0.0 0.0 0.0;
0.4300    D+  K0                           TSS;
0.4700    D0  K+                           TSS;
Enddecay
CDecay myD_s2*-
#
Decay myD(2S)0
0.6667    myD*+ pi-                        SVS;
0.3333    D*0 pi0                          SVS;
Enddecay
CDecay myanti-D(2S)0

Decay myD(2S)+
0.3333    myD*+ pi0                        SVS;
0.6667    D*0 pi+                          SVS;
Enddecay
CDecay myD(2S)-

Decay myD*(2S)0
0.3333    myD*+ pi-                        VVS_PWAVE 1.0 0.0 0.0 0.0 0.0 0.0;
0.1667    D*0 pi0                          VVS_PWAVE 1.0 0.0 0.0 0.0 0.0 0.0;
0.1667    D0  pi0                          VSS;
0.3333    D+  pi-                          VSS;
Enddecay
CDecay myanti-D*(2S)0

Decay myD*(2S)+
0.1667    myD*+ pi0                        VVS_PWAVE 1.0 0.0 0.0 0.0 0.0 0.0;
0.3333    D*0 pi+                          VVS_PWAVE 1.0 0.0 0.0 0.0 0.0 0.0;
0.1667    D+  pi0                          VSS;
0.3333    D0  pi+                          VSS;
Enddecay
CDecay myD*(2S)-

Decay myB_c-
0.04030    myanti-B_s0  mu-     anti-nu_mu    PHOTOS  PHSP;
0.05060    anti-B_s*0   mu-     anti-nu_mu    PHOTOS  PHSP;
0.00340    myanti-B0    mu-     anti-nu_mu    PHOTOS  PHSP;
0.00580    anti-B*0     mu-     anti-nu_mu    PHOTOS  PHSP;
0.000049   myD*-        D0                    SVS;
0.00033    myD*-        D*0                   SVV_HELAMP 1.0 0.0 1.0 0.0 1.0 0.0;
0.0000004  myD*-        anti-D0               SVS;
0.0000016  anti-D*0     myD*-                 SVV_HELAMP 1.0 0.0 1.0 0.0 1.0 0.0;
0.00028    J/psi        myD*-                 SVV_HELAMP 1.0 0.0 1.0 0.0 1.0 0.0;
0.16400    myanti-B_s0  pi-                   PHSP;
0.07200    rho-         myanti-B_s0           SVS;
0.01060    myanti-B_s0  K-                    PHSP;
0.00000    K*-          myanti-B_s0           SVS;
0.06500    anti-B_s*0   pi-                   SVS;
0.20200    anti-B_s*0   rho-                  SVV_HELAMP 1.0 0.0 1.0 0.0 1.0 0.0;
0.00370    anti-B_s*0   K-                    SVS;
0.00000    anti-B_s*0   K*-                   SVV_HELAMP 1.0 0.0 1.0 0.0 1.0 0.0;
0.01060    myanti-B0    pi-                   PHSP;
0.00960    rho-         myanti-B0             SVS;
0.00070    myanti-B0    K-                    PHSP;
0.00015    K*-          myanti-B0             SVS;
0.00950    anti-B*0     pi-                   SVS;
0.02570    anti-B*0     rho-                  SVV_HELAMP 1.0 0.0 1.0 0.0 1.0 0.0;
0.00055    anti-B*0     K-                    SVS;
0.00058    anti-B*0     K*-                   SVV_HELAMP 1.0 0.0 1.0 0.0 1.0 0.0;
0.00037    myB-         pi0                   PHSP;
0.00034    rho0         myB-                  SVS;
0.01980    myB-         K0                    PHSP;
0.00430    K*0          myB-                  SVS;
0.00033    B*-          pi0                   SVS;
0.00090    B*-          rho0                  SVV_HELAMP 1.0 0.0 1.0 0.0 1.0 0.0;
0.01600    B*-          K0                    SVS;
0.01670    B*-          K*0                   SVV_HELAMP 1.0 0.0 1.0 0.0 1.0 0.0;
Enddecay
CDecay myB_c+

End
"""
            ),
        ),
        parameterSets = cms.vstring('EvtGen130')
    ),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(
            'SoftQCD:nonDiffractive = on',
            'PTFilter:filter = on', # this turn on the filter
            'PTFilter:quarkToFilter = 5', # PDG id of q quark
            'PTFilter:scaleToFilter = 5.0',
#             'HardQCD:hardbbbar = on',
#             'PhaseSpace:pTHatMin = 100',
		),
        parameterSets = cms.vstring(
            'pythia8CommonSettings',
            'pythia8CP5Settings',
            'processParameters',
        ),
    ),
)

###### Filters ##########
DstFromBhadronFilter = cms.EDFilter(
    "PythiaFilterMultiAncestor",
    DaughterIDs     = cms.untracked.vint32 (  421,   211), # D0, pion+
    DaughterMaxEtas = cms.untracked.vdouble( 1.e9,  1.e9),
    DaughterMaxPts  = cms.untracked.vdouble( 1.e9,  1.e9),
    DaughterMinEtas = cms.untracked.vdouble(-1.e9, -1.e9),
    DaughterMinPts  = cms.untracked.vdouble( -1.0, -1.0 ),
    MaxEta          = cms.untracked.double ( 99.0),
    MinEta          = cms.untracked.double (-99.0),
    MinPt           = cms.untracked.double (-1.0),
    MotherIDs       = cms.untracked.vint32 (5), # a b-quark, short for any b-hadron
    ParticleID      = cms.untracked.int32  (413) # D*+
)

D0ToKpiFromDstFilter = cms.EDFilter(
    "PythiaFilterMultiAncestor",
    DaughterIDs     = cms.untracked.vint32 ( -321,   211), # K-, pion+ # this shitty piece of code is blissfully ignorant about CC https://github.com/cms-sw/cmssw/blob/1ae3be438887808e96fe9a07d72009e5db230208/GeneratorInterface/GenFilters/plugins/PythiaFilterMultiAncestor.cc#L190
    DaughterMaxEtas = cms.untracked.vdouble( 1.e9,  1.e9),
    DaughterMaxPts  = cms.untracked.vdouble( 1.e9,  1.e9),
    DaughterMinEtas = cms.untracked.vdouble(-1.e9, -1.e9),
    DaughterMinPts  = cms.untracked.vdouble(-1.0 , -1.0 ),
    MaxEta          = cms.untracked.double ( 99.0),
    MinEta          = cms.untracked.double (-99.0),
    MinPt           = cms.untracked.double (-1.0),
    MotherIDs       = cms.untracked.vint32 (413), # D*+
    ParticleID      = cms.untracked.int32  (421) # D0
)

DstMuMaxMassFilter = cms.EDFilter(
    "MCParticlePairFilter",
    ParticleID1    = cms.untracked.vint32(413), # D*+
    ParticleID2    = cms.untracked.vint32(13), # mu
    ParticleCharge = cms.untracked.int32(0), # opposite charge
    MaxInvMass     = cms.untracked.double(8.),
    MinPt          = cms.untracked.vdouble(-1., -1.),
    MinEta         = cms.untracked.vdouble(-1.e9, -1.e9),
    MaxEta         = cms.untracked.vdouble( 1.e9,  1.e9),
    Status         = cms.untracked.vint32(2, 1),
)

ProductionFilterSequence = cms.Sequence(
    generator +
    DstFromBhadronFilter +
    D0ToKpiFromDstFilter +
    DstMuMaxMassFilter
)
