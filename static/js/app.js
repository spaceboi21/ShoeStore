document.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(window.location.search);
    const sku = params.get('sku');
    const size = params.get('size');
    
    fetch(`/shoe_details?sku=${sku}&size=${size}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                document.getElementById("shoe-name").textContent = data.name;
                document.getElementById("sku").textContent = data.sku;
                document.getElementById("size").textContent = data.size;
                document.getElementById("release-date").textContent = data.release_date;
                document.getElementById("gender").textContent = data.gender;
                document.getElementById("app-price").textContent = `$${data.app_price}`;
                document.getElementById("recent-sale").textContent = `$${data.recent_sale}`;
                document.getElementById("consign-price").textContent = `$${data.consign_price}`;
                document.getElementById("liquidity-bar").value = data.liquidity;
                document.getElementById("shoe-image").src = data.image_url;
            }
        })
        .catch(error => console.error('Error fetching data:', error));
    
    document.getElementById("next-sneaker").addEventListener("click", () => {
        // Implement logic to fetch the next sneaker details
        console.log("Next sneaker button clicked");
    });
});
