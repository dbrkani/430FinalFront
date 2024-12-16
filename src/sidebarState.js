import React, { useState } from 'react';
import Cart from './Cart';

const sidebarState = () => {
    const [isCartOpen, setIsCartOpen] = useState(false);

    const toggleCart = () => {
        setIsCartOpen(prevState => !prevState);
    };

    const handleClose = () => {
        setIsCartOpen(false);
    };

    return (
        <div>
            <button onClick={toggleCart}>Open Cart</button>
            {isCartOpen && <Cart onClose={handleClose} />}
        </div>
    );
};

export default sidebarState;