import{ClienteLayout } from '../layouts';
import{Home, Emprendimientos } from '../Pages/Cliente';


const routesCliente = [
    {
        path: "/",
        layout: ClienteLayout,
        component: Home,
    },
    {
        path: "/emprendimientos",
        layout: ClienteLayout,
        component: Emprendimientos,
    },
];

export default routesCliente;
