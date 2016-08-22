import timeit
import sys



class Merge:
    def __init__(self):
        pass

    def merge_Sort(self, the_list):
        """Break up the lists on each iteration and pass them to the merge function"""
        if len(the_list) > 1:
            first_half  = the_list[ : len(the_list) // 2]
            second_half = the_list[len(the_list) // 2 :]
            
            self.merge_Sort(first_half)
            self.merge_Sort(second_half)

            self.merge_Them(first_half, second_half, the_list)



    def merge_Them(self, a_list, b_list, temp):
        """The merge_Them function handles the brunt work of the program and compares each lists index to finish a full sort"""
        a_list_index = 0
        b_list_index = 0
        temp_index   = 0

        while a_list_index < len(a_list) and b_list_index < len(b_list):
            if a_list[a_list_index] < b_list[b_list_index]:
                temp[temp_index] = a_list[a_list_index]
                a_list_index += 1
                temp_index   += 1
            else:
                temp[temp_index] = b_list[b_list_index]
                b_list_index += 1
                temp_index   += 1
        
        while a_list_index < len(a_list):
            temp[temp_index] = a_list[a_list_index]
            a_list_index += 1
            temp_index   += 1
        
        while b_list_index < len(b_list):
            temp[temp_index] = b_list[b_list_index]
            b_list_index += 1
            temp_index   += 1



    def main():
        """The main function that sets everything up and tracks time execution"""
        some_list = [2,3,2,5,6,1,-2,3,14,12]

        start = timeit.timeit()
        merge_Sort(some_list)
        finish = timeit.timeit()

        for thingy in some_list:
            print("{} ".format(thingy), end='')
        print()

        print("Merge sort took {:.6f} seconds to complete".format(finish - start))



    if __name__ == '__main__':
        sys.exit(int(main() or 0))
