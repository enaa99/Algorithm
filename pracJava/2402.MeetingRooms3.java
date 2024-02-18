import java.util.*;
class Solution {
    public int mostBooked(int n, int[][] meetings) {
        Arrays.sort(meetings, Comparator.comparingInt(a -> a[0]));
        List<Integer> freeRooms = new ArrayList<>();
        PriorityQueue<long[]> busyRooms = new PriorityQueue<>(Comparator.comparingLong((long[] a) -> a[0]).thenComparingLong((long[] a) -> a[1]));
        long[] count = new long[n];

        for (int i = 0; i < n; i++) {
            freeRooms.add(i);
        }

        for (int[] meeting : meetings) {
            int start = meeting[0];
            int end = meeting[1];

            while (!busyRooms.isEmpty() && busyRooms.peek()[0] <= start) {
                freeRooms.add((int) busyRooms.poll()[1]);
            }

            Collections.sort(freeRooms);

            //빈 방이 있을 때
            if (!freeRooms.isEmpty()) {
                long room = freeRooms.remove(0);
                busyRooms.offer(new long[]{end, room});
                count[(int) room]++;
            } else {
                long[] room = busyRooms.poll();
                long endTime = room[0];
                long prevRoom = room[1];
                endTime += (end - start);
                busyRooms.offer(new long[]{endTime, prevRoom});
                count[(int) prevRoom]++;
            }
        }

        long maxCount = Arrays.stream(count).max().getAsLong();
        for (int i = 0; i < n; i++) {
            if (count[i] == maxCount) {
                return i;
            }
        }

        return -1;
    }
}