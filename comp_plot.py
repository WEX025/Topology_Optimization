import matplotlib.pyplot as plt

class compliance():
    '''
    This module is to plot the change of compliance during optimization based on the Matlab calculation
    '''
    def extract(module_name):
    
        for file_id in range(1,6):
            file_name = "m"+str(module_name)+"_"+str(file_id)+".txt"
            # load files
            results = []
            with open(file_name) as inputfile:
                for line in inputfile:
                    results.append(line.strip().split())
 
            # extract the num of iteration and val of compliance
            results = [el for el in results if el]
            iter = []
            comp = []
            for each_row in results:
                if ("It.:" and "Obj.:") in each_row:
                    iter_ix = each_row.index("It.:")+1
                    iter.append(each_row[iter_ix])
                    comp_ix = each_row.index("Obj.:")+1
                    comp.append(each_row[comp_ix])

            labels = ["2:1", "1.5:1", "1:1", "1:1.5", "1:2"]
            # visualize
            plt.plot(iter, comp, label=labels[file_id-1])
            plt.legend()
            plt.xlabel("Iteration")
            plt.ylabel("Compliance")
        plt.show()