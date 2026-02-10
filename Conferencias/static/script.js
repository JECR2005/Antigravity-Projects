
document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const filterChips = document.querySelectorAll('.filter-chip');
    const scheduleItems = document.querySelectorAll('.schedule-item');
    const noResults = document.getElementById('noResults');

    let currentCategory = 'all';
    let searchQuery = '';

    function filterItems() {
        let visibleCount = 0;

        scheduleItems.forEach(item => {
            const title = item.dataset.title.toLowerCase();
            const speakers = item.dataset.speakers.toLowerCase();
            const categories = item.dataset.categories.toLowerCase();

            const matchesSearch = title.includes(searchQuery) ||
                speakers.includes(searchQuery) ||
                categories.includes(searchQuery);

            const matchesCategory = currentCategory === 'all' ||
                item.dataset.categories.includes(currentCategory);

            if (matchesSearch && matchesCategory) {
                item.classList.remove('hidden');
                visibleCount++;
            } else {
                item.classList.add('hidden');
            }
        });

        if (visibleCount === 0) {
            noResults.classList.remove('hidden');
        } else {
            noResults.classList.add('hidden');
        }
    }

    searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value.toLowerCase().trim();
        filterItems();
    });

    filterChips.forEach(chip => {
        chip.addEventListener('click', () => {
            // Remove active class from all
            filterChips.forEach(c => c.classList.remove('active'));
            // Add to clicked
            chip.classList.add('active');

            currentCategory = chip.dataset.filter;
            filterItems();
        });
    });
});
