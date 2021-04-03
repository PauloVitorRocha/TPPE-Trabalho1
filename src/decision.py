    def decision_stream_to_xml(self, f, k):
        f.write("\t\t\t<DecisionStream count=\"{}\">\n".format(k+1))
        a_count = 0
        m_count = 0
        f_count = 0
        for i in self.elements:
            if i == 0:
                f.write("\t\t\t\t<Activity name=\"{}\"/>\n".format(self.activity_node[a_count]))
                a_count += 1
            elif i == 1:
                f.write("\t\t\t\t<FinalNode name=\"{}\"/>\n".format(self.final_node[f_count]))
                f_count += 1
            elif i == 2:
                f.write("\t\t\t\t<MergeNode name=\"{}\"/>\n".format(self.merge_node[m_count]))
                m_count += 1
        
        f.write("\t\t\t\t<DecisionStreamTransitions>\n".format(k+1))
        for transition in self.transitions:
            transition.transition_to_xml(f, True)
        
        f.write("\t\t\t\t</DecisionStreamTransitions>\n")
        f.write("\t\t\t</DecisionStream>\n")

    
    
    

