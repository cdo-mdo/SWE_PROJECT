import { VehicleCard } from "@/components/VehicleCard";
import { vehicles } from "@/lib/mockData";
import { VehicleCategory } from "@shared/schema";
//import { useToast } from "@/hooks/use-toast"; //This import is no longer needed

export default function VehicleSelect() {
  //const { toast } = useToast(); //This is no longer needed

  //const handleSelectVehicle = (vehicle: VehicleCategory) => {
  //  toast({
  //    title: "Vehicle Selected",
  //    description: `You have selected the ${vehicle.name} - ${vehicle.description}`,
  //  });
  //};

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 py-4 sm:px-6 lg:px-8">
        <img
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTv8VCDlM64uFv7274Mn3UjHpqXRGtIwAWokg&s"
            alt="Rent logo"
            className="h-12"
          />
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-12 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">
          Select Your Vehicle
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {vehicles.map((vehicle) => (
            <VehicleCard
              key={vehicle.id}
              vehicle={vehicle}
            />
          ))}
        </div>
      </main>
    </div>
  );
}