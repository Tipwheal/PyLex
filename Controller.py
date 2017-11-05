import ReadLex
import PreProcessRE
import NFAGenerator
import ClosureGetter
import DFAGenerator
import DFAOGenerator
import ProgramWriter

ReadLex.read_lex("lex.l")
PreProcessRE.pre_p(ReadLex.pre_map)
NFAGenerator.generate(PreProcessRE.result_map, ReadLex.use_map.keys())
ClosureGetter.calc_closure()
DFAGenerator.get_transition_table()
DFAOGenerator.get_combine_list()
ProgramWriter.write("lex.yy.py")
