const defaultUrl = "http://127.0.0.1:8000";
export const url = {
    orders: `${defaultUrl}/orders`,
    dashboard: `${defaultUrl}/dashboard`,
    filters: `${defaultUrl}/filters`,
    details: `${defaultUrl}/orders/create/details`,
    create_order: `${defaultUrl}/orders/create`,
    companyOverview: {
        main: `${defaultUrl}/overview/company`,
        filters: `${defaultUrl}/overview/company/filters`,
    }
}