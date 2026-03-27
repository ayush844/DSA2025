class Solution {
    public int leastInterval(char[] tasks, int n) {
        // 1. count frequency of each task
        Map<Character, Integer> frequencyMap = new HashMap<>();
        for(char task: tasks){
            frequencyMap.put(task, frequencyMap.getOrDefault(task, 0) + 1);
        }

        // build maxheap based on the frequency
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b-a);
        maxHeap.addAll(frequencyMap.values());

        int time = 0;
        while(!maxHeap.isEmpty()){
            List<Integer> temp = new ArrayList<>();

            for(int i = 0; i < n+1; i++){
                if(!maxHeap.isEmpty()){
                    temp.add(maxHeap.poll());
                }
            }

            for(int freq : temp){
                if(--freq > 0){
                    maxHeap.add(freq);
                }
            }

            time += maxHeap.isEmpty() ? temp.size() : n+1;
        }

        return time;
    }
}