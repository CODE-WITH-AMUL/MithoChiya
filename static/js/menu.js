

    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Setup event listeners
    function setupEventListeners() {
        // Search input
        const searchInput = document.getElementById('menuSearch');
        if (searchInput) {
            searchInput.addEventListener('input', debounce(filterMenu, 300));
            searchInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    filterMenu();
                }
            });
        }
    }

    // Debounce utility function
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Filter menu items by search
    function filterMenu() {
        const searchInput = document.getElementById('menuSearch');
        if (!searchInput) return;

        const query = searchInput.value.toLowerCase().trim();
        const items = document.querySelectorAll('.menu-item');
        let visibleCount = 0;
        
        items.forEach((item, index) => {
            const name = item.getAttribute('data-name') || '';
            const category = item.getAttribute('data-category') || '';
            const description = item.getAttribute('data-description') || '';
            
            const matches = query === '' || 
                           name.includes(query) || 
                           category.includes(query) ||
                           description.includes(query);
            
            if (matches) {
                item.style.display = '';
                item.classList.add('animate-fade-in');
                visibleCount++;
            } else {
                item.style.display = 'none';
                item.classList.remove('animate-fade-in');
            }
        });

        // Show/hide no results message
        updateNoResultsMessage(visibleCount, query);
    }

    // Filter menu items by category
    function filterCategory(category) {
        // Update active button
        const buttons = document.querySelectorAll('.filter-btn');
        buttons.forEach(btn => {
            btn.classList.remove('active');
        });
        event.target.closest('.filter-btn').classList.add('active');

        // Filter items
        const items = document.querySelectorAll('.menu-item');
        let visibleCount = 0;

        items.forEach((item, index) => {
            const itemCategory = item.getAttribute('data-category') || '';
            const matches = category === 'all' || itemCategory === category;
            
            if (matches) {
                item.style.display = '';
                item.style.animationDelay = `${(index % 3) * 0.1}s`;
                item.classList.add('animate-fade-in');
                visibleCount++;
            } else {
                item.style.display = 'none';
                item.classList.remove('animate-fade-in');
            }
        });

        // Clear search when filtering by category
        const searchInput = document.getElementById('menuSearch');
        if (searchInput) {
            searchInput.value = '';
        }

        updateNoResultsMessage(visibleCount, '');
    }

    // Update no results message
    function updateNoResultsMessage(visibleCount, query) {
        const grid = document.getElementById('menuGrid');
        if (!grid) return;

        let noResults = grid.querySelector('.no-results');
        
        if (visibleCount === 0 && query !== '') {
            if (!noResults) {
                noResults = document.createElement('div');
                noResults.className = 'no-results animate-fade-in';
                noResults.innerHTML = `
                    <i class="bi bi-search no-results-icon"></i>
                    <h4 class="no-results-title">No items found</h4>
                    <p class="no-results-text">Try searching for something else</p>
                `;
                grid.appendChild(noResults);
            }
        } else if (noResults && (visibleCount > 0 || query === '')) {
            noResults.remove();
        }
    }

    // Add item to cart
    function addToCart(itemId, itemName, itemPrice) {
    const csrftoken = getCookie('csrftoken');

    fetch('/cart/add/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: `item_id=${itemId}&quantity=1`,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            updateCartUI(data.cart);
            showNotification('Item added to cart!', 'success');
        } else {
            showNotification(data.message || 'Error adding item.', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('An unexpected error occurred.', 'error');
    });
}

    // Change quantity
    function updateCart(itemId, quantity) {
    const csrftoken = getCookie('csrftoken');
    const url = quantity > 0 ? '/cart/update/' : '/cart/remove/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrftoken,
        },
        body: `item_id=${itemId}&quantity=${quantity}`,
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            updateCartUI(data.cart);
            if (quantity > 0) {
                showNotification('Cart updated!', 'success');
            } else {
                showNotification('Item removed from cart.', 'warning');
            }
        } else {
            showNotification(data.message || 'Error updating cart.', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('An unexpected error occurred.', 'error');
    });
}

    // Update cart UI
    function updateCartUI(cartData) {
        const container = document.getElementById('cartItemsContainer');
        const footer = document.getElementById('cartFooter');
        const cartCount = document.getElementById('cartCount');
        
        if (!container || !footer || !cartCount) return;

        container.innerHTML = '';
        let total = 0;
        let itemCount = 0;

        const keys = Object.keys(cartData);
        
        if (keys.length === 0) {
            container.innerHTML = `
                <div class="empty-cart">
                    <i class="bi bi-cart empty-cart-icon"></i>
                    <p class="empty-cart-text">Your cart is empty</p>
                    <p class="empty-cart-subtext">Add items from the menu to get started!</p>
                </div>`;
            footer.classList.add('d-none');
            cartCount.textContent = '0 items';
        } else {
            footer.classList.remove('d-none');
            
            keys.forEach(id => {
                const item = cartData[id];
                if (!item) return;

                total += parseFloat(item.price) * item.quantity;
                itemCount += item.quantity;
                
                const cartItem = document.createElement('div');
                cartItem.className = 'cart-item animate-fade-in';
                cartItem.innerHTML = `
                    <div class="cart-item-info">
                        <div class="cart-item-name">${escapeHtml(item.name)}</div>
                        <div class="cart-item-price">Rs ${parseFloat(item.price).toFixed(2)}</div>
                    </div>
                    <div class="quantity-controls">
                        <button class="qty-btn" onclick="updateCart('${id}', ${item.quantity - 1})" aria-label="Decrease quantity">
                            <i class="bi bi-dash"></i>
                        </button>
                        <span class="cart-item-qty">${item.quantity}</span>
                        <button class="qty-btn" onclick="updateCart('${id}', ${item.quantity + 1})" aria-label="Increase quantity">
                            <i class="bi bi-plus"></i>
                        </button>
                    </div>
                `;
                container.appendChild(cartItem);
            });
            
            cartCount.textContent = `${itemCount} item${itemCount !== 1 ? 's' : ''}`;
            
            const totalVal = document.getElementById('totalVal');
            if (totalVal) {
                totalVal.textContent = total.toFixed(2);
            }
        }
    }

    // Place order
    function placeOrder() {
    const csrftoken = getCookie('csrftoken');

    fetch('/order/place/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            updateCartUI({});
            showNotification(data.message, 'success');
        } else {
            showNotification(data.message || 'Error placing order.', 'error');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('An unexpected error occurred.', 'error');
    });
}

    // Show notification
    function showNotification(message, type = 'success') {
        // Remove existing notifications
        const existing = document.querySelectorAll('.notification');
        existing.forEach(n => n.remove());

        const notification = document.createElement('div');
        notification.className = `notification ${type} animate__animated animate__fadeInDown`;
        
        const iconMap = {
            success: 'check-circle-fill',
            warning: 'exclamation-triangle-fill',
            error: 'x-circle-fill'
        };
        
        notification.innerHTML = `
            <i class="bi bi-${iconMap[type]} notification-icon"></i>
            <span class="notification-message">${escapeHtml(message)}</span>
            <button class="notification-close" onclick="this.parentElement.remove()" aria-label="Close notification">
                <i class="bi bi-x"></i>
            </button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto remove after 3 seconds
        setTimeout(() => {
            if (notification.parentElement) {
                notification.classList.remove('animate__fadeInDown');
                notification.classList.add('animate__fadeOutUp');
                setTimeout(() => {
                    if (notification.parentElement) {
                        notification.remove();
                    }
                }, 300);
            }
        }, 3000);
    }

    // Escape HTML to prevent XSS
    function escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return String(text).replace(/[&<>"']/g, m => map[m]);
    }

    // Handle window resize
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            // Add any resize-specific logic here if needed
        }, 250);
    });