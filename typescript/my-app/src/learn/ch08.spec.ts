describe('ch08', () => {
    it('test_1', () => {
        const rainfall_mi = '1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85';
        const rainfall_string_array: string[] = rainfall_mi.split(',');
        let num_rainy_months = 0;
        for ( const rain_string of rainfall_string_array) {
            const rainfall = Number.parseFloat(rain_string);
            if (rainfall > 3.0) {
                 num_rainy_months ++;
            }
        }
        expect(num_rainy_months).toEqual(5);
    }); // it
}); // describe
