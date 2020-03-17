import FWCore.ParameterSet.Config as cms
from PhysicsTools.NanoAOD.nano_cff import *
from PhysicsTools.NanoAODJMAR.recluster_cff import *
#from PhysicsTools.NanoAOD.custom_jme_cff import *


nanoSequence += finalJetsAK8Constituents + finalJetsAK8ConstituentsTable + finalJetsAK4Constituents + finalJetsAK4ConstituentsTable

nanoSequenceMC += finalJetsAK8Constituents + genJetsAK8Constituents + finalJetsAK8ConstituentsTable + genJetsAK8ParticleTable+ finalJetsAK4Constituents + finalJetsAK4ConstituentsTable + genJetsAK4Constituents+ genJetsAK4ParticleTable



def nanoAOD_customizeData_JMAR(process):
    #process = PrepJMECustomNanoAOD(process, runOnMC=True)
    process = nanoAOD_customizeData(process)
    return process

def nanoAOD_customizeMC_JMAR(process):
    #process = PrepJMECustomNanoAOD(process, runOnMC=False)
    process = nanoAOD_customizeMC(process)
    return process
