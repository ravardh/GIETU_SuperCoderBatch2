
class Solution {
    public static ArrayList<Integer> duplicates(int arr[], int n) {
        // code here
       ArrayList<Integer> ans = new ArrayList<>();
        Arrays.sort(arr);
        
        for(int i=1; i<n; i++){
            if(arr[i]==arr[i-1]){
                //found duplicate
                ans.add(arr[i]);
                //go forward till its repeated
                while(i+1<n && arr[i+1]==arr[i]){
                    i = i+1;
                }
            }
            else{
                // do nothing
            }
        }
        if(ans.size()==0){
            ans.add(-1);
        }

        return ans;
    }
}
