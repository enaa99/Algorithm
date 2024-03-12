import java.util.*;
import java.util.stream.Collectors;


public class Solution {
    public String[] solution(String[] companies, String[] applicants) {
        Map<String, Queue<String>> applyMap = new HashMap<>();
        Map<String, List<String>> companyPreferences = new HashMap<>();
        Map<String, Integer> companyHireLimits = new HashMap<>();
        Map<String, Set<String>> finalSelections = new HashMap<>();

        setupApplicants(applicants, applyMap);
        setupCompanies(companies, companyPreferences, companyHireLimits, finalSelections);

        Set<String> alreadySelectedApplicants = new HashSet<>();

        Boolean updated = false;
        do {
            updated = false;

            // 지원자가 회사에 지원
            applyMap.forEach((applicant, preferences) -> {
                if (!preferences.isEmpty() && !alreadySelectedApplicants.contains(applicant)) {
                    String company = preferences.poll();
                    finalSelections.computeIfAbsent(company, k -> new HashSet<>()).add(applicant);
                }
            });

            // 지원리스트 초기화
            alreadySelectedApplicants.clear();
            // 회사별 지원자 처리
            for (Map.Entry<String, Set<String>> entry : finalSelections.entrySet()) {
                String company = entry.getKey();
                Set<String> applicantsForCompany = entry.getValue();

                List<String> sortedApplicants = sortApplicants(applicantsForCompany, companyPreferences.get(company), companyHireLimits.get(company));
                Set<String> selectedApplicants = new HashSet<>(sortedApplicants);

                // 업데이트가 필요한 경우
                if (!finalSelections.containsKey(company) || !finalSelections.get(company).equals(selectedApplicants)) {
                    updated = true;
                    finalSelections.put(company, selectedApplicants);
                }
                // 잠정 지원자 리스트에 새롭게 추가
                alreadySelectedApplicants.addAll(selectedApplicants); 
            }

        } while (updated);

        // 결과 생성 오름차순으로 정렬
        List<String> sortedResult = finalSelections.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .map(e -> {
                    List<String> sortedValues = e.getValue().stream().sorted().collect(Collectors.toList());
                    return e.getKey() + "_" + String.join("", sortedValues);
                })
                .collect(Collectors.toList());

        return sortedResult.toArray(new String[0]);
    }

    private List<String> sortApplicants(Set<String> applicants, List<String> preferences, int limit) {
        return applicants.stream()
                .sorted(Comparator.comparingInt(preferences::indexOf))
                .limit(limit)
                .collect(Collectors.toList());
    }


    private void setupApplicants(String[] applicants, Map<String, Queue<String>> applyMap) {
        for (String applicant : applicants) {
            String[] parts = applicant.split(" ");
            Queue<String> preferences = Arrays.stream(parts[1].split(""))
                                              .limit(Integer.parseInt(parts[2]))
                                              .collect(Collectors.toCollection(LinkedList::new));
            applyMap.put(parts[0], preferences);
        }
    }

    private void setupCompanies(String[] companies, Map<String, List<String>> companyPreferences, Map<String, Integer> companyHireLimits, Map<String, Set<String>> finalSelections) {
        for (String company : companies) {
            String[] parts = company.split(" ");
            List<String> preferences = Arrays.asList(parts[1].split(""));
            companyPreferences.put(parts[0], preferences);
            companyHireLimits.put(parts[0], Integer.parseInt(parts[2]));
            finalSelections.put(parts[0], new HashSet<>());
        }
    }
}
